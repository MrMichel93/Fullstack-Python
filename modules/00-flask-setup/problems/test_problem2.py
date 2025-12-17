"""
Tests for Problem 2: Dynamic Greeting App

Run with: pytest test_problem2.py -v
"""

import pytest
from problem2_greeting import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_greet_default(client):
    """Test default greeting route without name."""
    response = client.get('/greet')
    assert response.status_code == 200, "Greet route should return status 200"
    data = response.data.decode('utf-8')
    assert any(word in data.lower() for word in ['hello', 'hi', 'greetings', 'guest']), \
        "Default greeting should contain a greeting for guest"


def test_greet_with_name(client):
    """Test greeting with name parameter."""
    response = client.get('/greet/Alice')
    assert response.status_code == 200, "Greet with name should return status 200"
    data = response.data.decode('utf-8')
    assert 'Alice' in data, "Greeting should include the provided name"


def test_greet_with_different_names(client):
    """Test greeting works with different names."""
    names = ['Bob', 'Charlie', 'Diana']
    for name in names:
        response = client.get(f'/greet/{name}')
        data = response.data.decode('utf-8')
        assert name in data, f"Greeting should include the name {name}"


def test_greet_time_morning(client):
    """Test time-specific greeting for morning."""
    response = client.get('/greet/time?name=Alice&time=morning')
    assert response.status_code == 200, "Time greeting route should return status 200"
    data = response.data.decode('utf-8').lower()
    assert 'morning' in data and 'alice' in data, \
        "Morning greeting should contain 'morning' and the name"


def test_greet_time_afternoon(client):
    """Test time-specific greeting for afternoon."""
    response = client.get('/greet/time?name=Bob&time=afternoon')
    data = response.data.decode('utf-8').lower()
    assert 'afternoon' in data and 'bob' in data, \
        "Afternoon greeting should contain 'afternoon' and the name"


def test_greet_time_evening(client):
    """Test time-specific greeting for evening."""
    response = client.get('/greet/time?name=Charlie&time=evening')
    data = response.data.decode('utf-8').lower()
    assert 'evening' in data and 'charlie' in data, \
        "Evening greeting should contain 'evening' and the name"


def test_greet_time_no_name(client):
    """Test time greeting without name parameter (should use default)."""
    response = client.get('/greet/time?time=morning')
    assert response.status_code == 200, "Should work without name parameter"
    data = response.data.decode('utf-8').lower()
    assert 'morning' in data, "Should still show morning greeting"
    assert any(word in data for word in ['guest', 'hello', 'hi']), \
        "Should have default name or greeting"


def test_greet_time_no_time(client):
    """Test time greeting without time parameter (should use default)."""
    response = client.get('/greet/time?name=Alice')
    assert response.status_code == 200, "Should work without time parameter"
    data = response.data.decode('utf-8')
    assert 'Alice' in data, "Should include the provided name"


def test_greet_time_invalid_time(client):
    """Test time greeting with invalid time parameter."""
    response = client.get('/greet/time?name=Alice&time=midnight')
    assert response.status_code == 200, "Should handle invalid time gracefully"
    data = response.data.decode('utf-8')
    assert 'Alice' in data, "Should still include the name"
