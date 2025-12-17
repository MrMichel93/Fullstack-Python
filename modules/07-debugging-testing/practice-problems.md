# Practice Problems - Debugging & Testing

Sharpen your debugging and testing skills with these exercises:

## Problem 1: Add Logging to an Application
**Difficulty:** Easy  
**Time:** 20-25 minutes

Take an existing Flask application (or create a simple one) and add comprehensive logging:

**Requirements:**
1. Configure logging to write to both console and a file (`app.log`)
2. Add appropriate log levels:
   - **DEBUG**: Log all incoming requests (method, path, IP address)
   - **INFO**: Log successful operations (note created, user logged in)
   - **WARNING**: Log suspicious activity (failed login attempts, invalid input)
   - **ERROR**: Log all errors with stack traces
3. Create at least one route that demonstrates each log level
4. Test your logging by:
   - Making successful requests (check INFO logs)
   - Making requests with invalid data (check WARNING logs)
   - Triggering an error (check ERROR logs)

**Example routes to implement:**
```python
@app.route('/')  # Log INFO: Page accessed
@app.route('/calculate')  # Log WARNING: If invalid input
@app.route('/data/<int:id>')  # Log ERROR: If ID not found
```

**What you'll practice:**
- Configuring Python logging
- Using appropriate log levels
- Logging with context (user IDs, request details)
- Reading log files for debugging

---

## Problem 2: Debug the Broken Application
**Difficulty:** Medium  
**Time:** 25-30 minutes

A Flask notes application has several bugs. Use debugging techniques to find and fix them!

**Buggy Code (intentionally broken for learning purposes):**
```python
from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    db = sqlite3.connect('notes.db')
    return db

@app.route('/')
def index():
    db = get_db()
    notes = db.execute('SELECT * FROM notes').fetchall()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    db = get_db()
    db.execute(f"INSERT INTO notes (title, content) VALUES ('{title}', '{content}')")
    db.commit()
    return redirect('/')

@app.route('/delete/<id>')
def delete_note(id):
    db = get_db()
    db.execute('DELETE FROM notes WHERE id = ?', (id))  # BUG: Missing trailing comma in tuple
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
```

**Bugs to find and fix:**
1. Database connection not closed (memory leak)
2. SQL injection vulnerability in add_note
3. Missing database initialization
4. Wrong parameter type in delete_note
5. No error handling

**Your tasks:**
1. Use `logging` to trace the execution
2. Use `breakpoint()` to inspect variables
3. Fix all bugs
4. Add try-except error handling
5. Test that all operations work correctly

**What you'll practice:**
- Using debugger (pdb/breakpoint)
- Adding logging for diagnosis
- Identifying common bugs
- Database best practices
- Error handling

---

## Problem 3: Write Unit Tests
**Difficulty:** Medium  
**Time:** 30-35 minutes

Write comprehensive unit tests for a simple Flask calculator application:

**Application to test:**
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add')
def add():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({'result': a + b})

@app.route('/divide')
def divide():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 1))
    if b == 0:
        return jsonify({'error': 'Cannot divide by zero'}), 400
    return jsonify({'result': a / b})

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
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
```

**Tests to write:**
1. Test addition with positive numbers
2. Test addition with negative numbers
3. Test division by zero (should return 400 error)
4. Test divide route with valid inputs
5. Test calculate endpoint with all operations
6. Test calculate endpoint with invalid operation
7. Test calculate endpoint with missing parameters
8. Test calculate endpoint with invalid JSON

**Your test file structure:**
```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_positive_numbers(client):
    # Your test here
    pass

# Add more tests...
```

**What you'll practice:**
- Writing pytest tests
- Testing Flask routes
- Testing different scenarios (happy path, edge cases, errors)
- Using pytest fixtures
- Asserting response codes and data

**Bonus Challenge:**
- Add test for very large numbers
- Add test for decimal precision
- Measure test coverage with `pytest-cov`

---

## Quick Reference

### Print Debugging
```python
print(f"DEBUG: variable = {variable}")
print(f"DEBUG: type = {type(variable)}")
print(f"DEBUG: dir = {dir(variable)}")
```

### Logging
```python
logger.debug(f"Debug info: {data}")
logger.info(f"Important event")
logger.error(f"Error occurred: {e}", exc_info=True)
```

### Debugger
```python
breakpoint()  # Stop here
```

### Request Debugging (Flask)
```python
logger.debug(f"URL: {request.url}")
logger.debug(f"Method: {request.method}")
logger.debug(f"Form: {request.form}")
logger.debug(f"Args: {request.args}")
logger.debug(f"Headers: {request.headers}")
```

---

## Key Takeaways

1. **Use logging over print** - More powerful and flexible
2. **Learn the debugger** - Faster than print debugging
3. **Handle errors gracefully** - Try-except blocks
4. **Test early and often** - Catch bugs before they grow
5. **Read error messages carefully** - They tell you what's wrong
6. **Use version control** - Git helps track what changed
7. **Take breaks** - Fresh eyes find bugs faster

**Happy debugging!** 🐛🔍

---

**Done with the course?** Time to build your own projects! 🚀
