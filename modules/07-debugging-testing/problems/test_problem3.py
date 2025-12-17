"""
Practice Problem 3: Write Unit Tests

Difficulty: Medium
Time: 30-35 minutes

Write comprehensive unit tests for the Flask calculator application.

The calculator application (problem3_calculator.py) is already working.
Your task is to write tests to verify all its functionality.

Tests to write:
1. Test addition with positive numbers
2. Test addition with negative numbers
3. Test division by zero (should return 400 error)
4. Test divide route with valid inputs
5. Test calculate endpoint with all operations
6. Test calculate endpoint with invalid operation
7. Test calculate endpoint with missing parameters
8. Test calculate endpoint with invalid JSON

What you'll practice:
- Writing pytest tests
- Testing Flask routes
- Testing different scenarios (happy path, edge cases, errors)
- Using pytest fixtures
- Asserting response codes and data

Instructions:
1. Complete the TODO test functions below
2. Run tests with: pytest test_problem3.py -v
3. All tests should pass when you're done!

Hint: Look at the calculator code in problem3_calculator.py to understand
what to test and what the expected behavior is.
"""

import pytest
import json
from problem3_calculator import app


@pytest.fixture
def client():
    """
    Create a test client for the Flask app.
    
    This fixture is already provided for you.
    Use it in your test functions like: def test_something(client):
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# TODO: Write test for addition with positive numbers
def test_add_positive_numbers(client):
    """Test addition of two positive numbers."""
    # TODO: Send GET request to /add?a=10&b=5
    # TODO: Assert status code is 200
    # TODO: Assert result is 15
    pass


# TODO: Write test for addition with negative numbers
def test_add_negative_numbers(client):
    """Test addition with negative numbers."""
    # TODO: Send GET request to /add with negative numbers
    # TODO: Assert correct result
    pass


# TODO: Write test for addition with zero
def test_add_with_zero(client):
    """Test addition with zero."""
    # TODO: Test adding 0 to a number
    pass


# TODO: Write test for division with valid numbers
def test_divide_valid_numbers(client):
    """Test division with valid inputs."""
    # TODO: Send GET request to /divide?a=10&b=2
    # TODO: Assert result is 5
    pass


# TODO: Write test for division by zero
def test_divide_by_zero(client):
    """Test that dividing by zero returns error."""
    # TODO: Send GET request to /divide?a=10&b=0
    # TODO: Assert status code is 400
    # TODO: Assert response contains error message
    pass


# TODO: Write test for calculate with add operation
def test_calculate_add(client):
    """Test calculate endpoint with add operation."""
    # TODO: Send POST request to /calculate with JSON:
    #       {"operation": "add", "a": 5, "b": 3}
    # TODO: Assert result is 8
    pass


# TODO: Write test for calculate with subtract operation
def test_calculate_subtract(client):
    """Test calculate endpoint with subtract operation."""
    # TODO: Send POST with subtract operation
    # TODO: Assert correct result
    pass


# TODO: Write test for calculate with multiply operation
def test_calculate_multiply(client):
    """Test calculate endpoint with multiply operation."""
    # TODO: Send POST with multiply operation
    # TODO: Assert correct result
    pass


# TODO: Write test for calculate with divide operation
def test_calculate_divide(client):
    """Test calculate endpoint with divide operation."""
    # TODO: Send POST with divide operation
    # TODO: Assert correct result
    pass


# TODO: Write test for calculate with division by zero
def test_calculate_divide_by_zero(client):
    """Test calculate endpoint handles division by zero."""
    # TODO: Send POST with divide and b=0
    # TODO: Assert status code is 400
    # TODO: Assert error message
    pass


# TODO: Write test for calculate with invalid operation
def test_calculate_invalid_operation(client):
    """Test calculate endpoint with invalid operation."""
    # TODO: Send POST with invalid operation like "power"
    # TODO: Assert status code is 400
    # TODO: Assert error message
    pass


# TODO: Write test for calculate with missing JSON
def test_calculate_no_json(client):
    """Test calculate endpoint without JSON data."""
    # TODO: Send POST without JSON data
    # TODO: Assert status code is 400
    pass


# TODO: Write test for calculate with missing operation
def test_calculate_missing_operation(client):
    """Test calculate endpoint without operation field."""
    # TODO: Send POST with JSON but no 'operation' field
    # TODO: Check how it's handled
    pass


# TODO: Write test for calculate with missing parameters
def test_calculate_missing_parameters(client):
    """Test calculate endpoint with missing a or b."""
    # TODO: Send POST with operation but missing a or b
    # TODO: Check if defaults are used
    pass


# BONUS TODO: Write test for very large numbers
def test_add_large_numbers(client):
    """Bonus: Test addition with very large numbers."""
    # TODO: Test with large numbers
    pass


# BONUS TODO: Write test for decimal precision
def test_divide_decimal_precision(client):
    """Bonus: Test decimal precision in division."""
    # TODO: Test division that results in decimal
    pass


# Helper function example (you can use this in your tests)
def get_json_response(response):
    """Helper to get JSON from response."""
    return json.loads(response.data.decode('utf-8'))


# Example of a completed test (for reference):
def test_add_default_values(client):
    """Test addition with default values (no parameters)."""
    response = client.get('/add')
    assert response.status_code == 200
    data = get_json_response(response)
    assert 'result' in data
    assert data['result'] == 0  # 0 + 0 = 0
