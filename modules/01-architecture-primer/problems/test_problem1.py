"""
Tests for Problem 1: Trace the Request Journey

Run with: pytest test_problem1.py -v
"""

import pytest
from problem1_request_journey import (
    what_browser_does,
    what_http_method_for_viewing,
    what_server_receives,
    how_server_finds_route,
    what_server_does_with_database,
    what_server_sends_back,
    what_browser_does_with_response,
    trace_form_submission
)


def test_browser_steps_exist():
    """Test that browser steps are provided."""
    steps = what_browser_does()
    assert isinstance(steps, list), "Should return a list"
    assert len(steps) >= 3, "Should have at least 3 steps"
    assert all(isinstance(s, str) for s in steps), "All steps should be strings"


def test_browser_steps_content():
    """Test that browser steps mention key concepts."""
    steps = ' '.join(what_browser_does()).lower()
    # Should mention some of these concepts
    key_concepts = ['url', 'request', 'http', 'dns', 'server']
    assert any(concept in steps for concept in key_concepts), \
        "Browser steps should mention URL, request, or HTTP"


def test_http_method_for_viewing():
    """Test correct HTTP method for viewing."""
    method = what_http_method_for_viewing()
    assert method.upper() == 'GET', "Viewing a page should use GET method"


def test_server_receives_structure():
    """Test that server receives data has correct structure."""
    received = what_server_receives()
    assert isinstance(received, dict), "Should return a dictionary"
    assert 'method' in received or 'path' in received, \
        "Should include method or path information"


def test_server_receives_content():
    """Test that server receives appropriate data."""
    received = what_server_receives()
    if 'method' in received:
        assert received['method'].upper() in ['GET', 'POST', 'PUT', 'DELETE'], \
            "Method should be a valid HTTP method"
    if 'path' in received:
        assert '/profile' in received['path'] or 'john' in received['path'], \
            "Path should relate to the profile example"


def test_route_finding_explanation():
    """Test that route finding is explained."""
    explanation = how_server_finds_route()
    assert isinstance(explanation, str), "Should return a string"
    assert len(explanation) > 20, "Should be a meaningful explanation"
    # Should mention routing concepts
    keywords = ['route', 'match', 'pattern', 'url', 'path']
    assert any(keyword in explanation.lower() for keyword in keywords), \
        "Should explain route matching"


def test_database_steps_exist():
    """Test that database steps are provided."""
    steps = what_server_does_with_database()
    assert isinstance(steps, list), "Should return a list"
    assert len(steps) >= 3, "Should have at least 3 steps"


def test_database_steps_content():
    """Test that database steps mention relevant concepts."""
    steps = ' '.join(what_server_does_with_database()).lower()
    db_concepts = ['query', 'select', 'database', 'data', 'fetch', 'retrieve']
    assert any(concept in steps for concept in db_concepts), \
        "Should mention database or query operations"


def test_server_response_structure():
    """Test that server response has correct structure."""
    response = what_server_sends_back()
    assert isinstance(response, dict), "Should return a dictionary"
    # Should have some response components
    expected_keys = ['status_code', 'status', 'headers', 'body', 'content']
    assert any(key in response for key in expected_keys), \
        "Should include status_code, headers, or body"


def test_server_response_status():
    """Test that response includes valid status code."""
    response = what_server_sends_back()
    if 'status_code' in response:
        assert isinstance(response['status_code'], int), "Status code should be integer"
        assert 100 <= response['status_code'] < 600, "Should be valid HTTP status code"


def test_browser_response_handling():
    """Test that browser response handling steps exist."""
    steps = what_browser_does_with_response()
    assert isinstance(steps, list), "Should return a list"
    assert len(steps) >= 2, "Should have at least 2 steps"


def test_browser_response_content():
    """Test that browser response handling mentions key concepts."""
    steps = ' '.join(what_browser_does_with_response()).lower()
    concepts = ['parse', 'render', 'display', 'html', 'css', 'dom']
    assert any(concept in steps for concept in concepts), \
        "Should mention parsing, rendering, or displaying"


def test_form_submission_structure():
    """Test that form submission trace has correct structure."""
    form_trace = trace_form_submission()
    assert isinstance(form_trace, dict), "Should return a dictionary"
    expected_keys = ['http_method', 'data_direction', 'server_action', 'response_type']
    # Should have at least 2 of these keys
    matching_keys = sum(1 for key in expected_keys if key in form_trace)
    assert matching_keys >= 2, f"Should have at least 2 of: {expected_keys}"


def test_form_submission_method():
    """Test that form submission uses POST method."""
    form_trace = trace_form_submission()
    if 'http_method' in form_trace:
        assert form_trace['http_method'].upper() == 'POST', \
            "Form submission should use POST method"


def test_form_submission_mentions_update():
    """Test that form submission mentions updating data."""
    form_trace = trace_form_submission()
    trace_str = str(form_trace).lower()
    update_terms = ['update', 'modify', 'change', 'save', 'write']
    assert any(term in trace_str for term in update_terms), \
        "Should mention updating or modifying data"
