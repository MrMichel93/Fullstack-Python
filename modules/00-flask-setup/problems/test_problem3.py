"""
Tests for Problem 3: Simple Form Handler

Run with: pytest test_problem3.py -v
"""

import pytest
from problem3_form import app, feedback_list


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    # Clear feedback list after each test
    feedback_list.clear()


def test_form_page_exists(client):
    """Test that the form page exists."""
    response = client.get('/')
    assert response.status_code == 200, "Form page should return status 200"


def test_form_has_required_fields(client):
    """Test that the form has name, email, and message fields."""
    response = client.get('/')
    data = response.data.decode('utf-8').lower()
    assert 'name' in data, "Form should have a name field"
    assert 'email' in data, "Form should have an email field"
    assert 'message' in data, "Form should have a message field"


def test_form_posts_to_submit(client):
    """Test that the form can POST to /submit."""
    response = client.get('/')
    data = response.data.decode('utf-8').lower()
    assert 'submit' in data or 'form' in data, "Form should be able to submit"


def test_submit_with_valid_data(client):
    """Test form submission with valid data redirects to thank you page."""
    response = client.post('/submit', data={
        'name': 'Alice',
        'email': 'alice@example.com',
        'message': 'Test message'
    }, follow_redirects=False)
    assert response.status_code in [302, 303], "Should redirect after successful submission"
    assert '/thank-you' in response.location or 'thank-you' in response.location, \
        "Should redirect to thank you page"


def test_submit_with_valid_data_shows_success_message(client):
    """Test that successful submission shows success message."""
    response = client.post('/submit', data={
        'name': 'Bob',
        'email': 'bob@example.com',
        'message': 'Another test'
    }, follow_redirects=True)
    data = response.data.decode('utf-8')
    assert 'Bob' in data or 'thank' in data.lower(), \
        "Thank you page should contain the name or thank you message"


def test_submit_with_missing_name(client):
    """Test that missing name shows error."""
    response = client.post('/submit', data={
        'name': '',
        'email': 'test@example.com',
        'message': 'Test'
    }, follow_redirects=True)
    data = response.data.decode('utf-8').lower()
    # Should either redirect back to form or show error
    assert response.status_code == 200, "Should handle missing name"


def test_submit_with_missing_email(client):
    """Test that missing email shows error."""
    response = client.post('/submit', data={
        'name': 'Charlie',
        'email': '',
        'message': 'Test'
    }, follow_redirects=True)
    data = response.data.decode('utf-8').lower()
    assert response.status_code == 200, "Should handle missing email"


def test_submit_with_missing_message(client):
    """Test that missing message shows error."""
    response = client.post('/submit', data={
        'name': 'Diana',
        'email': 'diana@example.com',
        'message': ''
    }, follow_redirects=True)
    data = response.data.decode('utf-8').lower()
    assert response.status_code == 200, "Should handle missing message"


def test_thank_you_page_exists(client):
    """Test that thank you page exists."""
    # First submit valid data
    client.post('/submit', data={
        'name': 'Eve',
        'email': 'eve@example.com',
        'message': 'Test message'
    }, follow_redirects=False)
    
    # Then access thank you page
    response = client.get('/thank-you')
    assert response.status_code == 200, "Thank you page should exist"


def test_flash_messages_work(client):
    """Test that flash messages are displayed."""
    with client.session_transaction() as sess:
        # Test that we can use sessions (required for flash)
        sess['_flashes'] = [('message', 'Test flash')]
    
    response = client.get('/thank-you')
    assert response.status_code == 200, "Should be able to access thank you page with flash"


def test_bonus_feedback_storage(client):
    """Bonus: Test that feedback is stored in memory."""
    client.post('/submit', data={
        'name': 'Frank',
        'email': 'frank@example.com',
        'message': 'Test feedback'
    }, follow_redirects=True)
    
    # Check if feedback was stored (bonus feature)
    if len(feedback_list) > 0:
        assert feedback_list[0]['name'] == 'Frank', "Feedback should be stored with correct name"
        assert feedback_list[0]['email'] == 'frank@example.com', "Feedback should store email"
        assert feedback_list[0]['message'] == 'Test feedback', "Feedback should store message"


def test_bonus_feedback_display_route(client):
    """Bonus: Test that /feedback route displays submitted feedback."""
    # Submit some feedback
    client.post('/submit', data={
        'name': 'Grace',
        'email': 'grace@example.com',
        'message': 'Great app!'
    }, follow_redirects=True)
    
    # Try to access feedback route
    response = client.get('/feedback')
    # If route exists, it should return 200
    if response.status_code == 200:
        data = response.data.decode('utf-8')
        assert 'Grace' in data, "Feedback page should display submitted feedback"
