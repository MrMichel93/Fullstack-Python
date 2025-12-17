# Debugging & Testing

## 🐛 Why Debugging Matters

Every developer spends significant time debugging. Learning to debug efficiently will save you hours of frustration and make you a better programmer.

**This guide covers:**
1. Logging and print debugging
2. Using debuggers (pdb, IDE debuggers)
3. Error handling patterns
4. Testing strategies
5. Common debugging scenarios

---

## 1. Logging

### Why Logging > Print Statements

**Print statements:**
- Clutter your output
- No control over verbosity
- Disappear in production
- Can't be filtered or redirected

**Logging:**
- Different severity levels
- Can be toggled on/off
- Saved to files
- Includes timestamps and context

### Basic Logging Setup

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()  # Also print to console
    ]
)

logger = logging.getLogger(__name__)

# Use in your code
logger.debug("Detailed info for debugging")
logger.info("General information")
logger.warning("Something unexpected")
logger.error("Error occurred")
logger.critical("Critical error!")
```

### Logging Levels

```python
# DEBUG - Detailed information for diagnosing problems
logger.debug(f"User {user_id} requested page {page}")

# INFO - Confirmation things are working as expected
logger.info("Server started on port 5000")

# WARNING - Something unexpected, but app still works
logger.warning("Database connection slow (500ms)")

# ERROR - Error occurred, function failed
logger.error(f"Failed to save note {note_id}: {error}")

# CRITICAL - Serious error, app may not continue
logger.critical("Database connection lost!")
```

### Logging in Flask

```python
from flask import Flask

app = Flask(__name__)

# Flask has built-in logger
@app.route('/notes/<int:note_id>')
def get_note(note_id):
    app.logger.info(f"Fetching note {note_id}")
    
    try:
        note = fetch_note(note_id)
        app.logger.debug(f"Found note: {note}")
        return render_template('note.html', note=note)
    except Exception as e:
        app.logger.error(f"Error fetching note {note_id}: {e}")
        return "Error", 500
```

### Structured Logging

```python
# Log with context
logger.info("User logged in", extra={
    'user_id': user.id,
    'username': user.username,
    'ip': request.remote_addr,
    'user_agent': request.user_agent.string
})
```

---

## 2. Python Debugger (pdb)

### Basic pdb Usage

```python
import pdb

def problematic_function(data):
    # Set a breakpoint
    pdb.set_trace()  # Execution stops here
    
    result = process_data(data)
    return result

# When you run this, you'll get an interactive prompt:
# (Pdb) 
```

### pdb Commands

```
(Pdb) h          # Help - list all commands
(Pdb) l          # List code around current line
(Pdb) n          # Next line (step over)
(Pdb) s          # Step into function
(Pdb) c          # Continue execution
(Pdb) p var      # Print variable value
(Pdb) pp var     # Pretty-print variable
(Pdb) where      # Show stack trace
(Pdb) up         # Move up stack frame
(Pdb) down       # Move down stack frame
(Pdb) q          # Quit debugger
```

### Post-Mortem Debugging

```python
import pdb

try:
    # Code that might fail
    result = risky_operation()
except Exception:
    # Drop into debugger when error occurs
    pdb.post_mortem()
```

### Breakpoint in Python 3.7+

```python
# Modern way (Python 3.7+)
def problematic_function(data):
    breakpoint()  # Better than pdb.set_trace()
    result = process_data(data)
    return result
```

---

## 3. Error Handling

### Try-Except Patterns

**Basic Error Handling:**
```python
try:
    result = dangerous_operation()
except Exception as e:
    logger.error(f"Operation failed: {e}")
    return "Error occurred", 500
```

**Specific Exceptions:**
```python
try:
    note = db.execute("SELECT * FROM notes WHERE id=?", (note_id,)).fetchone()
except sqlite3.OperationalError as e:
    logger.error(f"Database error: {e}")
    return "Database error", 500
except sqlite3.IntegrityError as e:
    logger.error(f"Constraint violation: {e}")
    return "Invalid data", 400
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    return "Server error", 500
```

**Finally Block:**
```python
def save_note(note_data):
    db = get_db()
    try:
        db.execute("INSERT INTO notes VALUES (?, ?)", note_data)
        db.commit()
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()  # Always executed
```

**Else Block:**
```python
try:
    result = process_data(data)
except ValueError as e:
    logger.error(f"Invalid data: {e}")
else:
    # Only runs if no exception
    logger.info("Processing successful")
    return result
```

### Custom Exceptions

```python
class InvalidNoteError(Exception):
    """Raised when note data is invalid"""
    pass

class NoteNotFoundError(Exception):
    """Raised when note doesn't exist"""
    pass

def get_note(note_id):
    note = db.execute("SELECT * FROM notes WHERE id=?", (note_id,)).fetchone()
    if not note:
        raise NoteNotFoundError(f"Note {note_id} not found")
    return note

# Usage
try:
    note = get_note(123)
except NoteNotFoundError as e:
    logger.warning(str(e))
    return "Note not found", 404
```

### Error Pages in Flask

```python
@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 error: {request.url}")
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 error: {error}")
    db.session.rollback()  # Rollback any failed transactions
    return render_template('500.html'), 500
```

---

## 4. Testing Strategies

### Manual Testing Checklist

```
□ Happy path works (expected inputs)
□ Edge cases (empty, max size, special characters)
□ Invalid inputs (wrong type, missing, malformed)
□ Boundary conditions (0, -1, max value)
□ Database errors (connection lost, constraint violation)
□ Concurrent access (multiple users)
□ Performance (large datasets, many requests)
```

### Unit Testing with pytest

```python
# test_notes.py
import pytest
from app import app, init_db

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    app.config['DATABASE'] = ':memory:'  # In-memory database
    
    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

def test_create_note(client):
    """Test creating a note"""
    response = client.post('/notes', data={
        'title': 'Test Note',
        'content': 'Test content'
    })
    assert response.status_code == 302  # Redirect
    
    # Verify note was created
    response = client.get('/')
    assert b'Test Note' in response.data

def test_empty_note(client):
    """Test creating note with empty fields"""
    response = client.post('/notes', data={
        'title': '',
        'content': ''
    })
    # Should handle gracefully (redirect or error)
    assert response.status_code in [302, 400]

def test_edit_note(client):
    """Test editing a note"""
    # Create note
    client.post('/notes', data={'title': 'Original', 'content': 'Content'})
    
    # Edit note
    response = client.post('/notes/1/update', data={
        'title': 'Updated',
        'content': 'New content'
    })
    assert response.status_code == 302
    
    # Verify changes
    response = client.get('/')
    assert b'Updated' in response.data
    assert b'Original' not in response.data
```

### Running Tests

```bash
# Install pytest
pip install pytest

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest test_notes.py

# Run specific test
pytest test_notes.py::test_create_note

# Show print statements
pytest -s

# Stop on first failure
pytest -x
```

---

## 5. Common Debugging Scenarios

### Database Issues

**Problem:** "Database is locked"
```python
# Solution: Use context manager and short transactions
from contextlib import closing

with closing(get_db()) as db:
    db.execute("INSERT INTO notes VALUES (?, ?)", (title, content))
    db.commit()
# Connection automatically closed
```

**Problem:** "No such table"
```python
# Solution: Check if database initialized
import os

if not os.path.exists('notes.db'):
    logger.info("Database not found, initializing...")
    init_db()
```

**Problem:** "Column not found"
```python
# Solution: Check table schema
db = get_db()
cursor = db.execute("PRAGMA table_info(notes)")
columns = cursor.fetchall()
logger.debug(f"Table columns: {columns}")
```

### Template Issues

**Problem:** "Template not found"
```python
# Check templates directory
import os
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
logger.debug(f"Template directory: {template_dir}")
logger.debug(f"Files: {os.listdir(template_dir)}")
```

**Problem:** "Variable undefined in template"
```python
# Solution: Always pass variables to template
@app.route('/')
def index():
    notes = get_all_notes()
    # Pass variables explicitly
    return render_template('index.html', 
                         notes=notes,
                         user=current_user,
                         title="My Notes")
```

### Form Issues

**Problem:** "Form data not received"
```python
# Debug form submission
@app.route('/notes', methods=['POST'])
def create_note():
    logger.debug(f"Form data: {request.form}")
    logger.debug(f"Method: {request.method}")
    logger.debug(f"Content-Type: {request.content_type}")
    
    # Check field names match
    title = request.form.get('title')  # Safer than ['title']
    if not title:
        logger.warning("Title field missing or empty")
```

### Performance Issues

**Problem:** Slow page loads
```python
import time

@app.route('/notes')
def list_notes():
    start = time.time()
    
    notes = db.execute("SELECT * FROM notes").fetchall()
    query_time = time.time() - start
    logger.info(f"Query took {query_time:.3f}s")
    
    render_start = time.time()
    response = render_template('notes.html', notes=notes)
    render_time = time.time() - render_start
    logger.info(f"Render took {render_time:.3f}s")
    
    return response
```

---

## 6. Debugging Tools

### Flask Debug Toolbar

```python
# Install
pip install flask-debugtoolbar

# Setup
from flask_debugtoolbar import DebugToolbarExtension

app.config['SECRET_KEY'] = 'dev'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

# Shows:
# - SQL queries and execution time
# - Template rendering time
# - Request/response headers
# - Session data
```

### VS Code Debugging

**launch.json:**
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "app.py",
                "FLASK_DEBUG": "1"
            },
            "args": ["run"],
            "jinja": true
        }
    ]
}
```

### Browser DevTools

**Console Tab:**
- View JavaScript errors
- Test JavaScript code
- See console.log output

**Network Tab:**
- See all HTTP requests
- Check status codes
- View request/response headers
- See timing information

**Application Tab:**
- View cookies
- Check local storage
- Inspect session data

---

## 7. Best Practices

### Development vs Production

```python
import os

# Different configs for dev/prod
if os.getenv('FLASK_ENV') == 'development':
    app.config['DEBUG'] = True
    logging.basicConfig(level=logging.DEBUG)
else:
    app.config['DEBUG'] = False
    logging.basicConfig(level=logging.WARNING)
```

### Defensive Programming

```python
# Check assumptions
def divide(a, b):
    assert b != 0, "Cannot divide by zero"
    return a / b

# Validate inputs
def get_note(note_id):
    if not isinstance(note_id, int):
        raise TypeError(f"note_id must be int, got {type(note_id)}")
    if note_id < 1:
        raise ValueError(f"note_id must be positive, got {note_id}")
    # ... rest of function
```

### Code Reviews

- Use print statements/logging during development
- Remove debug code before committing
- Add comments explaining complex logic
- Write docstrings for functions
- Handle error cases explicitly

---

## 8. Debugging Workflow

1. **Reproduce the bug** - Can you make it happen consistently?
2. **Isolate the problem** - Which function/route is failing?
3. **Form a hypothesis** - What do you think is wrong?
4. **Test your hypothesis** - Add logging, use debugger
5. **Fix the issue** - Make minimal changes
6. **Verify the fix** - Test the original scenario
7. **Test edge cases** - Make sure you didn't break anything

---

## 9. Practice Problems

Ready to master debugging and testing? Complete the **[Practice Problems](./practice-problems.md)** to build your skills!

**What you'll work on:**
- Add comprehensive logging to a Flask application
- Debug and fix a broken application
- Write unit tests for a calculator API

These exercises help you develop professional debugging and testing practices.

---

## 10. Quick Reference

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

## 11. Key Takeaways

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
