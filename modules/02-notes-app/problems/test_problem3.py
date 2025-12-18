"""
Tests for Problem 3: Notes with Search

Run with: pytest test_problem3.py -v
"""

import pytest
from problem3_search import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_placeholder(client):
    """Placeholder test - implement your tests here."""
    assert True, "Replace this with actual tests"
