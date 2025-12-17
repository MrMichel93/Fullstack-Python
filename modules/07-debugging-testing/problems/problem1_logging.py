"""
Practice Problem 1: Add Logging to an Application

Difficulty: Easy
Time: 20-25 minutes

Configure logging for a Flask application with appropriate log levels.

Requirements:
1. Configure logging to write to both console and a file (app.log)
2. Add appropriate log levels:
   - DEBUG: Log all incoming requests (method, path, IP address)
   - INFO: Log successful operations
   - WARNING: Log suspicious activity (failed attempts, invalid input)
   - ERROR: Log all errors with stack traces
3. Create routes that demonstrate each log level

What you'll practice:
- Configuring Python logging
- Using appropriate log levels
- Logging with context (user IDs, request details)

Instructions:
1. Complete the TODO sections below
2. Run tests with: pytest test_problem1.py -v
"""

from flask import Flask, request
import logging

app = Flask(__name__)


# TODO: Configure logging
# - Set up logger with name 'flask_app'
# - Set level to DEBUG
# - Create console handler and file handler (app.log)
# - Set appropriate format: timestamp, level, message
# - Add handlers to logger

def configure_logging():
    """
    Configure logging for the application.
    
    TODO: Implement logging configuration
    
    Requirements:
    - Logger name: 'flask_app'
    - Level: DEBUG
    - Console handler: INFO level
    - File handler: DEBUG level, file='app.log'
    - Format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    """
    # TODO: Create and configure logger
    pass


# Get logger for use in routes
logger = logging.getLogger('flask_app')


# TODO: Add before_request handler to log all incoming requests
# Should log: method, path, and remote_addr at DEBUG level


@app.route('/')
def home():
    """
    Home page route.
    
    TODO: Add INFO level log for successful page access
    """
    # TODO: Log successful access
    return "Home Page"


@app.route('/calculate')
def calculate():
    """
    Calculate route that performs division.
    
    TODO: 
    - Log WARNING if parameters are missing or invalid
    - Log ERROR if division by zero occurs
    - Log INFO if calculation succeeds
    """
    try:
        a = request.args.get('a')
        b = request.args.get('b')
        
        # TODO: Log warning if parameters are missing
        if not a or not b:
            # TODO: Add WARNING log
            return "Missing parameters", 400
        
        # TODO: Log warning if parameters are not numeric
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            # TODO: Add WARNING log
            return "Invalid parameters", 400
        
        # TODO: Log error if division by zero
        if b == 0:
            # TODO: Add ERROR log
            return "Cannot divide by zero", 400
        
        result = a / b
        # TODO: Log successful calculation at INFO level
        return f"Result: {result}"
        
    except Exception as e:
        # TODO: Log unexpected errors at ERROR level with exception info
        return "Internal error", 500


@app.route('/data/<int:item_id>')
def get_item(item_id):
    """
    Get item by ID.
    
    TODO:
    - Log DEBUG for each access attempt
    - Log WARNING if ID is out of valid range
    - Log ERROR if item not found
    - Log INFO if item found successfully
    """
    # Simulate item database
    items = {1: "Item A", 2: "Item B", 3: "Item C"}
    
    # TODO: Log debug message with item_id
    
    # TODO: Log warning if ID is negative or too large
    if item_id < 0 or item_id > 100:
        # TODO: Add WARNING log
        return "Invalid ID", 400
    
    # TODO: Log error if item not found
    if item_id not in items:
        # TODO: Add ERROR log
        return "Item not found", 404
    
    # TODO: Log successful retrieval at INFO level
    return f"Item: {items[item_id]}"


if __name__ == '__main__':
    configure_logging()
    # Debug mode is enabled for learning/development purposes only
    # Never use debug=True in production!
    app.run(debug=True)
