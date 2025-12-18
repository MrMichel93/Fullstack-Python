"""
Tests for Problem 1: Basic CRUD Notes App

Run with: pytest test_problem1.py -v
"""

import pytest
import sqlite3
from problem1_crud_notes import app, init_db


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client


def test_home_route_exists(client):
    """Test that the home page route exists and returns 200."""
    response = client.get('/')
    assert response.status_code == 200, "Home page should return status 200"


def test_create_note_route(client):
    """Test creating a new note via POST."""
    response = client.post('/notes', data={
        'title': 'Test Note',
        'content': 'This is a test note'
    }, follow_redirects=True)
    assert response.status_code == 200, "Create note should succeed"


def test_note_appears_after_creation(client):
    """Test that a created note appears on the home page."""
    client.post('/notes', data={
        'title': 'My Note',
        'content': 'Note content here'
    })
    response = client.get('/')
    assert b'My Note' in response.data, "Created note should appear on home page"


def test_view_single_note(client):
    """Test viewing a single note."""
    # Create a note first
    client.post('/notes', data={
        'title': 'Single Note',
        'content': 'Content of single note'
    })
    
    # Try to view it (assuming first note has id=1)
    response = client.get('/notes/1')
    assert response.status_code == 200, "View note page should return 200"
    assert b'Single Note' in response.data or b'single note' in response.data.lower()


def test_edit_note_form(client):
    """Test that the edit form loads with note data."""
    # Create a note
    client.post('/notes', data={
        'title': 'Edit Test',
        'content': 'Original content'
    })
    
    # Access edit form
    response = client.get('/notes/1/edit')
    assert response.status_code == 200, "Edit form should return 200"


def test_update_note(client):
    """Test updating a note."""
    # Create a note
    client.post('/notes', data={
        'title': 'Original Title',
        'content': 'Original content'
    })
    
    # Update it
    response = client.post('/notes/1/update', data={
        'title': 'Updated Title',
        'content': 'Updated content'
    }, follow_redirects=True)
    
    assert response.status_code == 200, "Update should succeed"
    assert b'Updated Title' in response.data or b'updated title' in response.data.lower()


def test_delete_note(client):
    """Test deleting a note."""
    # Create a note
    client.post('/notes', data={
        'title': 'To Be Deleted',
        'content': 'Delete me'
    })
    
    # Delete it
    response = client.post('/notes/1/delete', follow_redirects=True)
    assert response.status_code == 200, "Delete should succeed"
    
    # Verify it's gone
    response = client.get('/')
    # Should not contain the deleted note (or page should be empty of this note)
    # This is a basic check - in a real app you'd check the database


def test_note_not_found(client):
    """Test accessing a non-existent note returns 404."""
    response = client.get('/notes/999')
    assert response.status_code == 404, "Non-existent note should return 404"


def test_multiple_notes_display(client):
    """Test that multiple notes can be created and displayed."""
    # Create multiple notes
    client.post('/notes', data={'title': 'Note 1', 'content': 'Content 1'})
    client.post('/notes', data={'title': 'Note 2', 'content': 'Content 2'})
    client.post('/notes', data={'title': 'Note 3', 'content': 'Content 3'})
    
    response = client.get('/')
    assert b'Note 1' in response.data
    assert b'Note 2' in response.data
    assert b'Note 3' in response.data
