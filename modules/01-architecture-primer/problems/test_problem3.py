"""
Tests for Problem 3: Debug the Architecture

Run with: pytest test_problem3.py -v
"""

import pytest
from problem3_debug_code import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# Bug 1 Tests: Contact form should accept POST
def test_contact_accepts_get(client):
    """Test that contact route still works with GET."""
    response = client.get('/contact')
    assert response.status_code == 200, "Contact should handle GET requests"


def test_contact_accepts_post(client):
    """Test that contact route accepts POST method."""
    response = client.post('/contact', data={'name': 'Alice'})
    assert response.status_code == 200, "Contact should accept POST method"
    assert 'Alice' in response.data.decode('utf-8'), "Should show submitted name"


def test_contact_handles_form_data(client):
    """Test that contact can handle form submissions."""
    response = client.post('/contact', data={'name': 'Bob'})
    data = response.data.decode('utf-8')
    assert 'Bob' in data, "Should display form data"


# Bug 2 Tests: Profile should handle missing parameters
def test_profile_without_parameter(client):
    """Test that profile handles missing username parameter."""
    response = client.get('/profile')
    # Should not crash (status 200, 400, or other valid response)
    assert response.status_code != 500, "Should not crash without parameter"


def test_profile_with_parameter(client):
    """Test that profile works with username parameter."""
    response = client.get('/profile?username=Charlie')
    assert response.status_code == 200, "Should work with username"
    assert 'Charlie' in response.data.decode('utf-8'), "Should display username"


def test_profile_default_value(client):
    """Test that profile provides default when username missing."""
    response = client.get('/profile')
    data = response.data.decode('utf-8')
    # Should show something (default, message, or be handled gracefully)
    assert len(data) > 0, "Should return some content even without parameter"


# Bug 3 Tests: Welcome should render HTML properly
def test_welcome_renders_html(client):
    """Test that HTML content is rendered, not escaped."""
    response = client.get('/welcome')
    data = response.data.decode('utf-8')
    # Should contain actual h1 tag, not escaped &lt;h1&gt;
    assert '<h1>' in data or 'Hello World' in data, "HTML should be rendered"
    # Should NOT show escaped HTML
    assert '&lt;h1&gt;' not in data, "HTML should not be escaped"


def test_welcome_displays_heading(client):
    """Test that welcome page shows the heading."""
    response = client.get('/welcome')
    data = response.data.decode('utf-8')
    assert 'Hello World' in data, "Should display the heading text"


# Bug 4 Tests: Delete should use POST or DELETE method
def test_delete_not_available_via_get(client):
    """Test that delete is safer (ideally not GET)."""
    # Note: This test checks if POST/DELETE is supported
    # GET might still work but POST is required
    response = client.post('/delete/1')
    # Should either work with POST or return method not allowed
    assert response.status_code in [200, 404, 405], \
        "Should handle POST method appropriately"


def test_delete_with_post_method(client):
    """Test that delete works with POST method."""
    response = client.post('/delete/5')
    # Should work or give appropriate response
    assert response.status_code != 500, "Should not crash with POST"


def test_delete_with_valid_id(client):
    """Test that delete handles valid item ID."""
    # Try with the safest method first
    response = client.post('/delete/3')
    if response.status_code == 405:  # Method not allowed
        # If POST not supported, try GET (less safe but might be implemented)
        response = client.get('/delete/3')
    
    # At least one method should work
    assert response.status_code == 200, "Delete should work with valid ID"


# Bug 5 Tests: Divide should handle errors gracefully
def test_divide_with_valid_numbers(client):
    """Test that divide works with valid numbers."""
    response = client.get('/divide?a=10&b=2')
    assert response.status_code == 200, "Should work with valid numbers"
    data = response.data.decode('utf-8')
    assert '5' in data, "Should calculate correct result"


def test_divide_handles_missing_parameters(client):
    """Test that divide handles missing parameters."""
    response = client.get('/divide')
    # Should not crash with 500 error
    assert response.status_code != 500, "Should handle missing parameters gracefully"


def test_divide_handles_missing_a(client):
    """Test that divide handles missing 'a' parameter."""
    response = client.get('/divide?b=5')
    assert response.status_code != 500, "Should handle missing 'a' gracefully"


def test_divide_handles_missing_b(client):
    """Test that divide handles missing 'b' parameter."""
    response = client.get('/divide?a=10')
    assert response.status_code != 500, "Should handle missing 'b' gracefully"


def test_divide_handles_division_by_zero(client):
    """Test that divide handles division by zero."""
    response = client.get('/divide?a=10&b=0')
    assert response.status_code != 500, "Should handle division by zero gracefully"
    # Should return error message or 400 status
    assert response.status_code in [200, 400], "Should handle zero division"


def test_divide_handles_invalid_numbers(client):
    """Test that divide handles non-numeric input."""
    response = client.get('/divide?a=hello&b=world')
    assert response.status_code != 500, "Should handle invalid input gracefully"


def test_all_routes_dont_crash(client):
    """Test that no route causes a server crash."""
    routes = [
        ('GET', '/contact'),
        ('POST', '/contact', {'name': 'Test'}),
        ('GET', '/profile'),
        ('GET', '/profile?username=test'),
        ('GET', '/welcome'),
        ('GET', '/delete/1'),
        ('POST', '/delete/1'),
        ('GET', '/divide?a=1&b=1'),
    ]
    
    for route_info in routes:
        if len(route_info) == 2:
            method, path = route_info
            data = None
        else:
            method, path, data = route_info
        
        if method == 'GET':
            response = client.get(path)
        else:
            response = client.post(path, data=data)
        
        assert response.status_code != 500, \
            f"{method} {path} should not crash (got 500 error)"
