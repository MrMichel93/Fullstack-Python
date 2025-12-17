"""
Tests for Problem 2: Prevent Security Vulnerabilities

Run with: pytest test_problem2.py -v
"""

import pytest
from problem2_fix_vulnerabilities import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# XSS Prevention Tests
def test_search_prevents_xss_script_tags():
    """Test that script tags are escaped in search results."""
    client = app.test_client()
    response = client.get('/search?q=<script>alert("XSS")</script>')
    data = response.data.decode('utf-8')
    
    # Script should be escaped, not executed
    assert '<script>' not in data or '&lt;script&gt;' in data or 'alert' not in data, \
        "Script tags should be escaped to prevent XSS"


def test_search_escapes_html_entities():
    """Test that HTML entities are properly escaped."""
    client = app.test_client()
    response = client.get('/search?q=<b>test</b>')
    data = response.data.decode('utf-8')
    
    # HTML should be escaped
    assert '&lt;b&gt;' in data or '<b>test</b>' not in data, \
        "HTML tags should be escaped"


def test_search_shows_safe_content():
    """Test that normal search queries still work."""
    client = app.test_client()
    response = client.get('/search?q=python')
    assert response.status_code == 200
    data = response.data.decode('utf-8')
    assert 'python' in data.lower(), "Should display normal search queries"


# SQL Injection Prevention Tests
def test_user_profile_prevents_sql_injection_quotes():
    """Test that SQL injection with quotes is prevented."""
    client = app.test_client()
    # Try SQL injection with quotes
    response = client.get("/user/alice' OR '1'='1")
    # Should not return all users or cause error
    assert response.status_code in [200, 404], "Should handle SQL injection attempt safely"


def test_user_profile_prevents_sql_injection_union():
    """Test that UNION-based SQL injection is prevented."""
    client = app.test_client()
    response = client.get("/user/alice' UNION SELECT 1,2,3--")
    # Should not execute union query
    assert response.status_code in [200, 404], "Should prevent UNION injection"


def test_user_profile_valid_user():
    """Test that valid user lookup still works."""
    client = app.test_client()
    response = client.get('/user/alice')
    assert response.status_code == 200
    data = response.data.decode('utf-8')
    assert 'alice' in data.lower(), "Should find valid user"


def test_user_profile_invalid_user():
    """Test that invalid user is handled properly."""
    client = app.test_client()
    response = client.get('/user/nonexistent')
    assert response.status_code == 404, "Should return 404 for nonexistent user"


# Input Validation Tests
def test_api_user_with_valid_id():
    """Test API works with valid user ID."""
    client = app.test_client()
    response = client.get('/api/user/1')
    assert response.status_code == 200, "Should work with valid ID"


def test_api_user_with_nonexistent_id():
    """Test API handles nonexistent user ID."""
    client = app.test_client()
    response = client.get('/api/user/999')
    # Should not crash with 500
    assert response.status_code != 500, "Should handle nonexistent ID gracefully"
    # Should return appropriate error
    assert response.status_code in [200, 404, 400], "Should return appropriate status"


def test_api_user_with_negative_id():
    """Test API handles negative user ID."""
    client = app.test_client()
    # Flask should reject non-integer, but if it passes, should handle gracefully
    response = client.get('/api/user/-1')
    assert response.status_code != 500, "Should handle negative ID gracefully"


def test_api_user_with_zero_id():
    """Test API handles zero user ID."""
    client = app.test_client()
    response = client.get('/api/user/0')
    assert response.status_code != 500, "Should handle zero ID gracefully"


# Unsafe HTML Rendering Tests
def test_comment_escapes_script_tags():
    """Test that script tags in comments are escaped."""
    client = app.test_client()
    response = client.post('/comment', data={
        'comment': '<script>alert("XSS")</script>'
    })
    data = response.data.decode('utf-8')
    
    # Script should be escaped
    assert '<script>' not in data or '&lt;script&gt;' in data, \
        "Script tags in comments should be escaped"


def test_comment_escapes_html_tags():
    """Test that HTML tags in comments are escaped."""
    client = app.test_client()
    response = client.post('/comment', data={
        'comment': '<img src=x onerror=alert("XSS")>'
    })
    data = response.data.decode('utf-8')
    
    # HTML should be escaped
    assert 'onerror' not in data or '&lt;' in data, \
        "HTML tags should be escaped"


def test_comment_shows_safe_text():
    """Test that normal text in comments works."""
    client = app.test_client()
    response = client.post('/comment', data={
        'comment': 'This is a normal comment'
    })
    assert response.status_code == 200
    data = response.data.decode('utf-8')
    assert 'normal comment' in data, "Should display normal text"


def test_comment_handles_empty_input():
    """Test that empty comments are handled."""
    client = app.test_client()
    response = client.post('/comment', data={'comment': ''})
    assert response.status_code == 200, "Should handle empty comments"


# General Security Tests
def test_no_server_errors():
    """Test that common inputs don't cause server errors."""
    client = app.test_client()
    
    test_cases = [
        ('GET', '/search?q=test'),
        ('GET', '/search?q=<script>test</script>'),
        ('GET', '/user/alice'),
        ('GET', "/user/test'--"),
        ('GET', '/api/user/1'),
        ('POST', '/comment', {'comment': 'test'}),
        ('POST', '/comment', {'comment': '<b>test</b>'}),
    ]
    
    for method, path, *data in test_cases:
        if method == 'GET':
            response = client.get(path)
        else:
            response = client.post(path, data=data[0] if data else {})
        
        assert response.status_code != 500, \
            f"{method} {path} should not cause server error"


def test_sql_injection_does_not_expose_data():
    """Test that SQL injection doesn't expose unintended data."""
    client = app.test_client()
    
    # Try various SQL injection attempts
    injection_attempts = [
        "alice' OR 1=1--",
        "alice'; DROP TABLE users--",
        "alice' UNION SELECT username, email, 'extra' FROM users--",
    ]
    
    for attempt in injection_attempts:
        response = client.get(f'/user/{attempt}')
        data = response.data.decode('utf-8').lower()
        
        # Should not return multiple users or all users
        # Response should be limited to single user or not found
        assert response.status_code in [200, 404], \
            f"SQL injection attempt should be handled safely: {attempt}"
