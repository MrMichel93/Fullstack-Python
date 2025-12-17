"""
Practice Problem 1: Trace the Request Journey

Difficulty: Easy
Time: 10-15 minutes

Scenario: A user visits http://myapp.com/profile/john to view John's profile.

Complete the functions below to demonstrate understanding of the request/response lifecycle.

What you'll practice:
- Understanding the request/response lifecycle
- HTTP methods (GET vs POST)
- Client-server communication

Instructions:
1. Complete the TODO functions below
2. Run tests with: pytest test_problem1.py -v
"""


def what_browser_does():
    """
    Return a list of steps the browser takes when user enters a URL.
    
    TODO: Complete this function to return a list of strings describing
    what the browser does. Each string should be a step.
    
    Example steps might include:
    - Parse the URL
    - Make DNS lookup
    - Send HTTP request
    - etc.
    """
    # TODO: Return a list of steps (at least 3)
    return []


def what_http_method_for_viewing():
    """
    Return the HTTP method used when viewing a profile page.
    
    TODO: Return the appropriate HTTP method as a string.
    Should be one of: 'GET', 'POST', 'PUT', 'DELETE'
    """
    # TODO: Return the correct HTTP method
    return ""


def what_server_receives():
    """
    Return a dictionary describing what the server receives.
    
    TODO: Return a dict with keys like 'method', 'path', 'headers', etc.
    
    Example:
    {
        'method': 'GET',
        'path': '/profile/john',
        'headers': {...},
        'query_params': {...}
    }
    """
    # TODO: Return a dictionary describing the request
    return {}


def how_server_finds_route():
    """
    Return a string explaining how the server finds the right route.
    
    TODO: Explain how Flask or a web framework matches the URL to a route handler.
    """
    # TODO: Return an explanation (1-2 sentences)
    return ""


def what_server_does_with_database():
    """
    Return a list of steps the server takes to get data from database.
    
    TODO: List the steps to query user data from a database.
    """
    # TODO: Return a list of steps (at least 3)
    return []


def what_server_sends_back():
    """
    Return a dictionary describing the HTTP response.
    
    TODO: Return a dict with 'status_code', 'headers', 'body'
    
    Example:
    {
        'status_code': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': '<html>...</html>'
    }
    """
    # TODO: Return a dictionary describing the response
    return {}


def what_browser_does_with_response():
    """
    Return a list of steps the browser takes after receiving the response.
    
    TODO: List what the browser does with the HTML response.
    """
    # TODO: Return a list of steps (at least 3)
    return []


def trace_form_submission():
    """
    Return a dictionary describing what changes when user submits a form
    to edit their profile, compared to just viewing it.
    
    TODO: Return a dict with keys:
    - 'http_method': The HTTP method for form submission
    - 'data_direction': Where data flows (e.g., "client to server")
    - 'server_action': What the server does (e.g., "updates database")
    - 'response_type': What the server sends back
    """
    # TODO: Return a dictionary describing form submission
    return {}
