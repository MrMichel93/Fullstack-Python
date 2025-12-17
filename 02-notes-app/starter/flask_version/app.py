"""
Notes App - Flask Version
A simple CRUD application for managing notes

Learning objectives:
- Database connections and queries
- Form handling with POST requests
- Template rendering with dynamic data
- Basic routing and redirects
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'notes.db'


def get_db():
    """Create a database connection"""
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row  # Enables dict-style access: row['column_name']
    return db


def init_db():
    """Initialize the database with notes table"""
    db = get_db()
    # TODO: Create the notes table
    # Table should have: id (INTEGER PRIMARY KEY), title (TEXT), 
    # content (TEXT), created_at (TIMESTAMP)
    # Hint: Use db.execute() with CREATE TABLE IF NOT EXISTS
    
    # Your code here:
    pass
    
    db.commit()
    db.close()


@app.route('/')
def index():
    """Display all notes on the home page"""
    db = get_db()
    
    # TODO: Fetch all notes from the database
    # Hint: SELECT * FROM notes ORDER BY created_at DESC
    # Use db.execute().fetchall()
    
    notes = []  # Replace this with your query result
    
    db.close()
    return render_template('index.html', notes=notes)


@app.route('/notes', methods=['POST'])
def create_note():
    """Handle creating a new note"""
    # TODO: Get the title and content from the form
    # Hint: Use request.form['field_name']
    
    title = None  # Get from form
    content = None  # Get from form
    
    # TODO: Validate that both fields have content
    # If empty, you could return an error or redirect back
    
    # TODO: Insert the new note into the database
    # Hint: INSERT INTO notes (title, content) VALUES (?, ?)
    # Don't forget to commit!
    
    db = get_db()
    # Your code here:
    
    db.commit()
    db.close()
    
    # Redirect back to home page
    return redirect(url_for('index'))


@app.route('/notes/<int:note_id>/edit')
def edit_note(note_id):
    """Display the edit form for a specific note"""
    db = get_db()
    
    # TODO: Fetch the note with the given ID
    # Hint: SELECT * FROM notes WHERE id = ?
    # Use db.execute().fetchone()
    
    note = None  # Replace with your query
    
    db.close()
    
    if note is None:
        return "Note not found", 404
    
    return render_template('edit.html', note=note)


@app.route('/notes/<int:note_id>/update', methods=['POST'])
def update_note(note_id):
    """Handle updating an existing note"""
    # TODO: Get the updated title and content from the form
    
    title = None  # Get from form
    content = None  # Get from form
    
    # TODO: Update the note in the database
    # Hint: UPDATE notes SET title=?, content=? WHERE id=?
    
    db = get_db()
    # Your code here:
    
    db.commit()
    db.close()
    
    return redirect(url_for('index'))


@app.route('/notes/<int:note_id>/delete', methods=['POST'])
def delete_note(note_id):
    """Handle deleting a note"""
    # TODO: Delete the note with the given ID
    # Hint: DELETE FROM notes WHERE id=?
    
    db = get_db()
    # Your code here:
    
    db.commit()
    db.close()
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    # Initialize database on first run
    init_db()
    
    # Run the Flask development server
    print("🚀 Notes App is running!")
    print("📝 Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
