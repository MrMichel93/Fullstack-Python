"""
Tests for Problem 1: Basic URL Shortener

Run with: pytest test_problem1.py -v
"""

import pytest
from problem1_basic_shortener import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_placeholder(client):
    """Placeholder test - implement your tests here."""
    assert True, "Replace this with actual tests"
