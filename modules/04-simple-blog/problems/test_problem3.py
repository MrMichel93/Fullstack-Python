"""
Tests for Problem 3

Run with: pytest test_problem3.py -v
"""

import pytest
from problem3_placeholder import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_placeholder(client):
    assert True, "Replace with actual tests"
