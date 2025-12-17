"""
Flask Calculator Application

This is a working application for Problem 3.

Your task is to write comprehensive tests for this application
in the test_problem3.py file.

This calculator provides:
- Addition endpoint (GET /add?a=x&b=y)
- Division endpoint (GET /divide?a=x&b=y)
- Multi-operation endpoint (POST /calculate with JSON)

All code below is working correctly. Your job is to test it!
"""

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/add')
def add():
    """
    Add two numbers.
    
    Query parameters:
    - a: First number (default: 0)
    - b: Second number (default: 0)
    
    Returns:
        JSON: {'result': sum of a and b}
    """
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({'result': a + b})


@app.route('/divide')
def divide():
    """
    Divide two numbers.
    
    Query parameters:
    - a: Numerator (default: 0)
    - b: Denominator (default: 1)
    
    Returns:
        JSON: {'result': a / b}
        Or: {'error': 'Cannot divide by zero'} with status 400
    """
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 1))
    
    if b == 0:
        return jsonify({'error': 'Cannot divide by zero'}), 400
    
    return jsonify({'result': a / b})


@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Perform calculation based on operation.
    
    JSON Body:
    {
        'operation': 'add' | 'subtract' | 'multiply' | 'divide',
        'a': number,
        'b': number
    }
    
    Returns:
        JSON: {'result': calculated value}
        Or: {'error': error message} with status 400
    """
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'No JSON data provided'}), 400
    
    operation = data.get('operation')
    a = data.get('a', 0)
    b = data.get('b', 0)
    
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            return jsonify({'error': 'Cannot divide by zero'}), 400
        result = a / b
    else:
        return jsonify({'error': 'Invalid operation'}), 400
    
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
