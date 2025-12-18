"""
Tests for Problem 2: Notes with Categories

Run with: pytest test_problem2.py -v
"""

import pytest
from problem2_categories import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_placeholder(client):
    """Placeholder test - implement your tests here."""
    assert True, "Replace this with actual tests"
