# Notes App - CRUD Operations & Databases

## What You'll Learn
- CRUD operations (Create, Read, Update, Delete)
- SQLite database connections
- SQL queries (SELECT, INSERT, UPDATE, DELETE)
- Form data handling
- HTML forms (input, textarea, buttons)
- Template rendering with Jinja2
- Dynamic content display
- Basic CSS styling

---

## 1. CRUD Operations Overview

### What is CRUD?

**CRUD** stands for the four basic operations on persistent storage:

- **Create** - Add new records to the database
- **Read** - Retrieve and display existing records
- **Update** - Modify existing records
- **Delete** - Remove records from the database

Almost every web application uses CRUD operations to manage data.

### CRUD in Web Applications

| Operation | HTTP Method | SQL Query | Example URL |
|-----------|-------------|-----------|-------------|
| Create | POST | INSERT | POST /notes |
| Read | GET | SELECT | GET /notes or GET /notes/1 |
| Update | POST/PUT | UPDATE | POST /notes/1/update |
| Delete | POST/DELETE | DELETE | POST /notes/1/delete |

---

## 2. SQLite Database Basics

### What is SQLite?

SQLite is a **lightweight, file-based database** that:
- Doesn't require a separate server
- Stores data in a single file
- Perfect for learning and small applications
- Built into Python (no installation needed)

### Creating a Database Connection

```python
import sqlite3

def get_db():
    """Create a database connection."""
    db = sqlite3.connect('notes.db')
    db.row_factory = sqlite3.Row  # Access columns by name
    return db
```

### Creating Tables

```python
def init_db():
    """Initialize the database with tables."""
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.commit()
    db.close()
```

---

## 3. SQL Query Patterns

### Create (INSERT)

```python
@app.route('/notes', methods=['POST'])
def create_note():
    title = request.form['title']
    content = request.form['content']
    
    db = get_db()
    db.execute(
        'INSERT INTO notes (title, content) VALUES (?, ?)',
        (title, content)
    )
    db.commit()
    db.close()
    
    return redirect(url_for('index'))
```

### Read (SELECT)

```python
# Get all notes
@app.route('/')
def index():
    db = get_db()
    notes = db.execute('SELECT * FROM notes ORDER BY created_at DESC').fetchall()
    db.close()
    return render_template('index.html', notes=notes)

# Get single note
@app.route('/notes/<int:note_id>')
def view_note(note_id):
    db = get_db()
    note = db.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()
    db.close()
    
    if note is None:
        return "Note not found", 404
    
    return render_template('view_note.html', note=note)
```

### Update (UPDATE)

```python
@app.route('/notes/<int:note_id>/update', methods=['POST'])
def update_note(note_id):
    title = request.form['title']
    content = request.form['content']
    
    db = get_db()
    db.execute(
        'UPDATE notes SET title = ?, content = ? WHERE id = ?',
        (title, content, note_id)
    )
    db.commit()
    db.close()
    
    return redirect(url_for('view_note', note_id=note_id))
```

### Delete (DELETE)

```python
@app.route('/notes/<int:note_id>/delete', methods=['POST'])
def delete_note(note_id):
    db = get_db()
    db.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    db.commit()
    db.close()
    
    return redirect(url_for('index'))
```

---

## 4. Form Handling

### HTML Form for Creating Notes

```html
<form method="POST" action="/notes">
    <div>
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
    </div>
    
    <div>
        <label for="content">Content:</label>
        <textarea id="content" name="content" rows="10" required></textarea>
    </div>
    
    <button type="submit">Save Note</button>
</form>
```

### Processing Form Data in Flask

```python
from flask import request

@app.route('/notes', methods=['POST'])
def create_note():
    # Get form data
    title = request.form['title']
    content = request.form['content']
    
    # Validate data
    if not title or not content:
        flash('Title and content are required!', 'error')
        return redirect(url_for('new_note'))
    
    # Save to database
    db = get_db()
    db.execute(
        'INSERT INTO notes (title, content) VALUES (?, ?)',
        (title, content)
    )
    db.commit()
    db.close()
    
    flash('Note created successfully!', 'success')
    return redirect(url_for('index'))
```

---

## 5. Template Rendering with Jinja2

### Displaying a List of Notes

```html
<!-- index.html -->
{% extends "base.html" %}

{% block title %}My Notes{% endblock %}

{% block content %}
    <h1>My Notes</h1>
    
    <a href="/notes/new">Create New Note</a>
    
    {% if notes %}
        <div class="notes-list">
            {% for note in notes %}
                <div class="note-card">
                    <h2>{{ note.title }}</h2>
                    <p>{{ note.content[:100] }}{% if note.content|length > 100 %}...{% endif %}</p>
                    <small>Created: {{ note.created_at }}</small>
                    
                    <div class="actions">
                        <a href="/notes/{{ note.id }}">View</a>
                        <a href="/notes/{{ note.id }}/edit">Edit</a>
                        <form method="POST" action="/notes/{{ note.id }}/delete" style="display:inline;">
                            <button type="submit" onclick="return confirm('Delete this note?')">Delete</button>
                        </form>
                    </div>
                </div>
            {% endfor %}
        </div>
    {% else %}
        <p>No notes yet. <a href="/notes/new">Create your first note!</a></p>
    {% endif %}
{% endblock %}
```

### Edit Form with Pre-filled Data

```html
<!-- edit_note.html -->
{% extends "base.html" %}

{% block content %}
    <h1>Edit Note</h1>
    
    <form method="POST" action="/notes/{{ note.id }}/update">
        <div>
            <label for="title">Title:</label>
            <input type="text" id="title" name="title" value="{{ note.title }}" required>
        </div>
        
        <div>
            <label for="content">Content:</label>
            <textarea id="content" name="content" rows="10" required>{{ note.content }}</textarea>
        </div>
        
        <button type="submit">Update Note</button>
        <a href="/notes/{{ note.id }}">Cancel</a>
    </form>
{% endblock %}
```

---

## 6. Database Best Practices

### Always Use Parameterized Queries

**BAD - SQL Injection Vulnerability:**
```python
# NEVER do this!
query = f"SELECT * FROM notes WHERE id = {note_id}"
db.execute(query)
```

**GOOD - Safe from SQL Injection:**
```python
db.execute('SELECT * FROM notes WHERE id = ?', (note_id,))
```

### Close Database Connections

```python
# Always close connections
db = get_db()
try:
    result = db.execute('SELECT * FROM notes').fetchall()
finally:
    db.close()
```

Or use context managers:
```python
from contextlib import closing

with closing(get_db()) as db:
    result = db.execute('SELECT * FROM notes').fetchall()
# Automatically closed
```

### Handle Database Errors

```python
import sqlite3

@app.route('/notes/<int:note_id>')
def view_note(note_id):
    try:
        db = get_db()
        note = db.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()
        db.close()
        
        if note is None:
            return "Note not found", 404
        
        return render_template('view_note.html', note=note)
    except sqlite3.Error as e:
        app.logger.error(f"Database error: {e}")
        return "Database error", 500
```

---

## 7. Common Patterns

### Flash Messages for User Feedback

```python
from flask import flash

@app.route('/notes', methods=['POST'])
def create_note():
    title = request.form['title']
    content = request.form['content']
    
    db = get_db()
    db.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
    db.commit()
    db.close()
    
    flash('Note created successfully!', 'success')
    return redirect(url_for('index'))
```

Display in template:
```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }}">{{ message }}</div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

### URL Parameters for Dynamic Routing

```python
@app.route('/notes/<int:note_id>')
def view_note(note_id):
    # note_id is automatically converted to integer
    # /notes/5 -> note_id = 5
    pass

@app.route('/user/<username>')
def profile(username):
    # /user/john -> username = "john"
    pass
```

---

## 8. Basic CSS Styling

### Styling the Notes List

```css
/* static/css/style.css */
.notes-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.note-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.note-card h2 {
    margin-top: 0;
    color: #333;
}

.note-card p {
    color: #666;
    line-height: 1.6;
}

.note-card small {
    color: #999;
    font-size: 0.85em;
}

.actions {
    margin-top: 15px;
    display: flex;
    gap: 10px;
}

.actions a, .actions button {
    padding: 5px 15px;
    text-decoration: none;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.actions button:hover {
    background-color: #0056b3;
}
```

---

## 9. Practice Problems

Ready to build a notes application? Complete the **[Practice Problems](./practice-problems.md)** to apply what you've learned!

**What you'll build:**
- Full CRUD notes application
- Database-driven content
- Form handling and validation
- Dynamic templates
- Basic styling

These exercises will help you master database operations and form handling.

---

## 10. Quick Reference

### Database Operations

```python
# Connect
db = sqlite3.connect('notes.db')
db.row_factory = sqlite3.Row

# Create table
db.execute('CREATE TABLE IF NOT EXISTS notes (...)')

# Insert
db.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
db.commit()

# Select all
notes = db.execute('SELECT * FROM notes').fetchall()

# Select one
note = db.execute('SELECT * FROM notes WHERE id = ?', (id,)).fetchone()

# Update
db.execute('UPDATE notes SET title = ? WHERE id = ?', (title, id))
db.commit()

# Delete
db.execute('DELETE FROM notes WHERE id = ?', (id,))
db.commit()

# Close
db.close()
```

### Form Handling

```python
# In template
<form method="POST" action="/notes">
    <input name="title">
    <textarea name="content"></textarea>
    <button type="submit">Save</button>
</form>

# In Flask
@app.route('/notes', methods=['POST'])
def create_note():
    title = request.form['title']
    content = request.form['content']
    # ... process data
```

---

## 11. Next Steps

After completing this module:

1. ✅ You understand CRUD operations
2. ✅ You can work with SQLite databases
3. ✅ You can handle forms in Flask
4. ✅ You can render dynamic templates

**Continue to:** [URL Shortener](../03-url-shortener/) to learn about redirects and unique ID generation.

---

## 12. Resources

### SQLite Documentation
- SQLite Tutorial: https://www.sqlitetutorial.net/
- SQLite Python: https://docs.python.org/3/library/sqlite3.html

### Flask & Databases
- Flask Database Pattern: https://flask.palletsprojects.com/patterns/sqlite3/
- Flask Forms: https://flask.palletsprojects.com/patterns/wtforms/

---

**Ready to build with databases?** Head to [Practice Problems](./practice-problems.md)!
