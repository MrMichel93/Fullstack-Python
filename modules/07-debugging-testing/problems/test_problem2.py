"""
Tests for Problem 2: Debug the Broken Application

Run with: pytest test_problem2.py -v
"""

import pytest
import sqlite3
import os
from problem2_debug_bugs import app, init_db


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    # Clean up any existing database
    if os.path.exists('notes.db'):
        os.remove('notes.db')
    
    # Initialize database
    init_db()
    
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    
    # Clean up after tests
    if os.path.exists('notes.db'):
        try:
            os.remove('notes.db')
        except:
            pass


def test_database_initialized():
    """Test that database is properly initialized."""
    if os.path.exists('notes.db'):
        os.remove('notes.db')
    
    init_db()
    
    # Check that database file exists
    assert os.path.exists('notes.db'), "Database file should be created"
    
    # Check that notes table exists
    db = sqlite3.connect('notes.db')
    cursor = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='notes'")
    table = cursor.fetchone()
    db.close()
    
    assert table is not None, "Notes table should exist"
    
    # Clean up
    os.remove('notes.db')


def test_index_page_loads(client):
    """Test that index page loads without error."""
    response = client.get('/')
    assert response.status_code == 200, "Index page should load successfully"


def test_add_note_valid_data(client):
    """Test adding a note with valid data."""
    response = client.post('/add', data={
        'title': 'Test Note',
        'content': 'Test Content'
    }, follow_redirects=False)
    
    # Should redirect after successful add
    assert response.status_code in [302, 303], "Should redirect after adding note"


def test_add_note_appears_in_list(client):
    """Test that added note appears in the list."""
    client.post('/add', data={
        'title': 'My Note',
        'content': 'My Content'
    })
    
    response = client.get('/')
    data = response.data.decode('utf-8')
    assert 'My Note' in data, "Added note should appear in list"


def test_add_note_with_quotes(client):
    """Test that notes with quotes are handled correctly (SQL injection prevention)."""
    # Try to add a note with quotes (potential SQL injection)
    response = client.post('/add', data={
        'title': "Test's Note",
        'content': "Content with 'quotes'"
    }, follow_redirects=True)
    
    assert response.status_code == 200, "Should handle quotes in input"
    data = response.data.decode('utf-8')
    assert "Test's Note" in data or "Test&#39;s Note" in data, "Should display note with quotes"


def test_add_note_prevents_sql_injection(client):
    """Test that SQL injection in add_note is prevented."""
    # Try SQL injection through title
    response = client.post('/add', data={
        'title': "'; DROP TABLE notes; --",
        'content': "malicious content"
    }, follow_redirects=True)
    
    # Should not crash
    assert response.status_code == 200, "Should handle SQL injection attempt"
    
    # Check that table still exists by making another request
    response2 = client.get('/')
    assert response2.status_code == 200, "Table should still exist after injection attempt"


def test_delete_note(client):
    """Test deleting a note."""
    # First add a note
    client.post('/add', data={
        'title': 'To Delete',
        'content': 'Delete me'
    })
    
    # Get the note ID from database
    db = sqlite3.connect('notes.db')
    cursor = db.execute('SELECT id FROM notes WHERE title = ?', ('To Delete',))
    row = cursor.fetchone()
    db.close()
    
    if row:
        note_id = row[0]
        # Delete the note
        response = client.post(f'/delete/{note_id}')
        assert response.status_code in [200, 302, 303], "Delete should succeed"


def test_delete_nonexistent_note(client):
    """Test deleting a non-existent note."""
    # Try to delete note with ID 9999
    response = client.post('/delete/9999')
    # Should not crash with 500
    assert response.status_code != 500, "Should handle non-existent note gracefully"


def test_search_with_query(client):
    """Test search with valid query."""
    # Add a note to search for
    client.post('/add', data={
        'title': 'Searchable Note',
        'content': 'Find me'
    })
    
    response = client.get('/search?q=Searchable')
    assert response.status_code == 200, "Search should work with query"


def test_search_without_query(client):
    """Test search without query parameter."""
    response = client.get('/search')
    # Should not crash with 500
    assert response.status_code != 500, "Should handle missing query parameter"


def test_search_with_empty_query(client):
    """Test search with empty query."""
    response = client.get('/search?q=')
    assert response.status_code == 200, "Should handle empty query"


def test_multiple_operations(client):
    """Test multiple operations in sequence."""
    # Add multiple notes
    client.post('/add', data={'title': 'Note 1', 'content': 'Content 1'})
    client.post('/add', data={'title': 'Note 2', 'content': 'Content 2'})
    
    # List notes
    response = client.get('/')
    data = response.data.decode('utf-8')
    assert 'Note 1' in data and 'Note 2' in data, "Should display multiple notes"
    
    # Search for notes
    response = client.get('/search?q=Note')
    assert response.status_code == 200, "Search should work"


def test_database_connections_closed():
    """Test that database connections are properly closed."""
    # This is tricky to test directly, but we can check for errors
    # after many operations (which would fail if connections leak)
    if os.path.exists('notes.db'):
        os.remove('notes.db')
    
    init_db()
    client = app.test_client()
    
    # Perform many operations
    for i in range(20):
        client.post('/add', data={
            'title': f'Note {i}',
            'content': f'Content {i}'
        })
    
    # Should still be able to access the app
    response = client.get('/')
    assert response.status_code == 200, "Should handle many operations without connection leak"
    
    # Clean up
    if os.path.exists('notes.db'):
        os.remove('notes.db')


def test_no_crashes_on_common_inputs(client):
    """Test that common inputs don't cause crashes."""
    test_cases = [
        ('GET', '/'),
        ('POST', '/add', {'title': 'Test', 'content': 'Test'}),
        ('POST', '/add', {'title': "Test's", 'content': 'Test'}),
        ('GET', '/search?q=test'),
        ('GET', '/search?q='),
        ('POST', '/delete/1'),
        ('POST', '/delete/999'),
    ]
    
    for test in test_cases:
        method = test[0]
        path = test[1]
        data = test[2] if len(test) > 2 else None
        
        if method == 'GET':
            response = client.get(path)
        else:
            response = client.post(path, data=data)
        
        assert response.status_code != 500, \
            f"{method} {path} should not cause server error"


def test_sql_injection_in_various_fields(client):
    """Test that SQL injection is prevented in various input fields."""
    injection_attempts = [
        {'title': "'; DROP TABLE notes; --", 'content': 'test'},
        {'title': "test", 'content': "'; DELETE FROM notes; --"},
        {'title': "' OR '1'='1", 'content': 'test'},
    ]
    
    for data in injection_attempts:
        response = client.post('/add', data=data, follow_redirects=True)
        assert response.status_code == 200, "Should handle SQL injection attempts"
    
    # Verify app still works
    response = client.get('/')
    assert response.status_code == 200, "App should still work after injection attempts"
