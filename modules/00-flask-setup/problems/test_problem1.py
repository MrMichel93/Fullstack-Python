"""
Tests for Problem 1: Personal Portfolio Page

Run with: pytest test_problem1.py -v
"""

import pytest
from problem1_portfolio import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_route_exists(client):
    """Test that the home page route exists and returns 200."""
    response = client.get('/')
    assert response.status_code == 200, "Home page should return status 200"


def test_about_route_exists(client):
    """Test that the about page route exists and returns 200."""
    response = client.get('/about')
    assert response.status_code == 200, "About page should return status 200"


def test_contact_route_exists(client):
    """Test that the contact page route exists and returns 200."""
    response = client.get('/contact')
    assert response.status_code == 200, "Contact page should return status 200"


def test_home_contains_content(client):
    """Test that home page contains expected content."""
    response = client.get('/')
    data = response.data.decode('utf-8').lower()
    # Check for common welcome-type words
    assert any(word in data for word in ['welcome', 'home', 'hello', 'hi']), \
        "Home page should contain a welcome message"


def test_about_contains_content(client):
    """Test that about page contains information."""
    response = client.get('/about')
    data = response.data.decode('utf-8').lower()
    # Check for common about-type words
    assert any(word in data for word in ['about', 'information', 'bio', 'profile']), \
        "About page should contain information about you"


def test_contact_contains_email(client):
    """Test that contact page contains email information."""
    response = client.get('/contact')
    data = response.data.decode('utf-8').lower()
    # Check for email-related content
    assert any(word in data for word in ['email', 'contact', '@', 'mail']), \
        "Contact page should contain email or contact information"


def test_pages_have_navigation(client):
    """Test that pages have navigation links."""
    pages = ['/', '/about', '/contact']
    for page in pages:
        response = client.get(page)
        data = response.data.decode('utf-8').lower()
        # Check if there are multiple page references (indicating navigation)
        page_references = sum(1 for p in ['home', 'about', 'contact'] if p in data)
        assert page_references >= 2, f"Page {page} should have navigation to other pages"
