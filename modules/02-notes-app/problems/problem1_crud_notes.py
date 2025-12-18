"""
Practice Problem 1: Basic CRUD Notes App

Difficulty: Medium
Time: 30-40 minutes

Create a Flask application with complete CRUD functionality for notes:
- Display all notes on the home page (/)
- Create a new note with a form (/notes/new GET to show form, POST to /notes to create)
- View a single note (/notes/<id>)
- Edit a note (/notes/<id>/edit GET to show form, POST to /notes/<id>/update to update)
- Delete a note (POST to /notes/<id>/delete)
- Use SQLite database with a notes table (id, title, content, created_at)

What you'll practice:
- All four CRUD operations
- Database queries (INSERT, SELECT, UPDATE, DELETE)
- Form handling with GET and POST methods
- Dynamic routing with parameters

Instructions:
1. Complete the TODO sections below
2. Run tests with: pytest test_problem1.py -v
"""

from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def get_db():
    """Create a database connection."""
    db = sqlite3.connect(':memory:')  # Use in-memory database for testing
    db.row_factory = sqlite3.Row
    return db


def init_db():
    """Initialize the database with notes table."""
    # TODO: Create the notes table with columns:
    # - id (INTEGER PRIMARY KEY AUTOINCREMENT)
    # - title (TEXT NOT NULL)
    # - content (TEXT NOT NULL)
    # - created_at (TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    pass


# TODO: Create route for home page (/)
# Should display all notes from the database
# Order by created_at DESC (newest first)


# TODO: Create route to show new note form (GET /notes/new)
# Should render a form with title and content fields


# TODO: Create route to create a note (POST /notes)
# Should get title and content from request.form
# Insert into database and redirect to home page


# TODO: Create route to view a single note (GET /notes/<int:note_id>)
# Should fetch the note from database and display it
# Return 404 if note doesn't exist


# TODO: Create route to show edit form (GET /notes/<int:note_id>/edit)
# Should fetch the note and render an edit form with pre-filled data


# TODO: Create route to update a note (POST /notes/<int:note_id>/update)
# Should get title and content from request.form
# Update the note in database and redirect to view page


# TODO: Create route to delete a note (POST /notes/<int:note_id>/delete)
# Should delete the note from database and redirect to home page


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
