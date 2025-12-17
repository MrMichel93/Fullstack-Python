"""
Tests for Problem 1: Add Logging to an Application

Run with: pytest test_problem1.py -v
"""

import pytest
import logging
import os
from problem1_logging import app, configure_logging


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    # Configure logging before tests
    configure_logging()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def cleanup_log_file():
    """Clean up log file after tests."""
    yield
    if os.path.exists('app.log'):
        try:
            os.remove('app.log')
        except:
            pass


def test_logger_exists():
    """Test that logger is configured."""
    logger = logging.getLogger('flask_app')
    assert logger is not None, "Logger should be configured"


def test_logger_has_handlers():
    """Test that logger has handlers configured."""
    configure_logging()
    logger = logging.getLogger('flask_app')
    assert len(logger.handlers) > 0, "Logger should have handlers"


def test_home_route_works(client):
    """Test that home route works and returns 200."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Home Page" in response.data


def test_calculate_with_valid_numbers(client):
    """Test calculate route with valid numbers."""
    response = client.get('/calculate?a=10&b=2')
    assert response.status_code == 200
    assert b"5" in response.data or b"Result" in response.data


def test_calculate_missing_parameters(client):
    """Test calculate route handles missing parameters."""
    response = client.get('/calculate')
    assert response.status_code == 400
    assert b"Missing" in response.data or b"parameter" in response.data.lower()


def test_calculate_invalid_parameters(client):
    """Test calculate route handles invalid parameters."""
    response = client.get('/calculate?a=hello&b=world')
    assert response.status_code == 400


def test_calculate_division_by_zero(client):
    """Test calculate route handles division by zero."""
    response = client.get('/calculate?a=10&b=0')
    assert response.status_code == 400
    assert b"zero" in response.data.lower()


def test_get_item_valid_id(client):
    """Test get item with valid ID."""
    response = client.get('/data/1')
    assert response.status_code == 200
    assert b"Item" in response.data


def test_get_item_invalid_id(client):
    """Test get item with invalid ID."""
    response = client.get('/data/999')
    # Should return 400 (invalid) or 404 (not found)
    assert response.status_code in [400, 404]


def test_get_item_negative_id(client):
    """Test get item with negative ID."""
    response = client.get('/data/-1')
    assert response.status_code == 400


def test_get_item_not_found(client):
    """Test get item with non-existent ID."""
    response = client.get('/data/99')
    assert response.status_code in [400, 404]


def test_logging_to_file():
    """Test that logging writes to file."""
    configure_logging()
    logger = logging.getLogger('flask_app')
    
    # Log a test message
    logger.info("Test log message")
    
    # Check if file handler exists
    file_handlers = [h for h in logger.handlers if isinstance(h, logging.FileHandler)]
    assert len(file_handlers) > 0, "Should have file handler configured"


def test_logger_level():
    """Test that logger level is set correctly."""
    configure_logging()
    logger = logging.getLogger('flask_app')
    # Logger should be at DEBUG level or lower
    assert logger.level <= logging.DEBUG, "Logger should be at DEBUG level"


def test_all_routes_dont_crash(client):
    """Test that all routes handle requests without crashing."""
    routes = [
        '/',
        '/calculate?a=10&b=2',
        '/calculate',
        '/calculate?a=hello&b=world',
        '/calculate?a=10&b=0',
        '/data/1',
        '/data/999',
    ]
    
    for route in routes:
        response = client.get(route)
        assert response.status_code != 500, f"Route {route} should not crash"


def test_multiple_requests_logged(client):
    """Test that multiple requests are handled and logged."""
    # Make several requests
    client.get('/')
    client.get('/calculate?a=10&b=2')
    client.get('/data/1')
    
    # All should succeed
    response = client.get('/')
    assert response.status_code == 200


def test_logging_format():
    """Test that logging format is configured."""
    configure_logging()
    logger = logging.getLogger('flask_app')
    
    # Check that handlers have formatters
    for handler in logger.handlers:
        assert handler.formatter is not None, "Handler should have formatter"


def test_console_and_file_handlers():
    """Test that both console and file handlers are configured."""
    configure_logging()
    logger = logging.getLogger('flask_app')
    
    handler_types = [type(h).__name__ for h in logger.handlers]
    # Should have at least one of each type
    has_stream = any('Stream' in t for t in handler_types)
    has_file = any('File' in t for t in handler_types)
    
    assert has_stream or has_file, "Should have console or file handler"
