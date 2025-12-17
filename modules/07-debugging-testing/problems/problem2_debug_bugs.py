"""
Practice Problem 2: Debug the Broken Application

Difficulty: Medium
Time: 25-30 minutes

A Flask notes application has several bugs. Find and fix them!

⚠️ This code is intentionally broken for learning purposes!

Bugs to find and fix:
1. Database connection not closed (memory leak)
2. SQL injection vulnerability in add_note
3. Missing database initialization
4. Wrong parameter type in delete_note
5. No error handling

What you'll practice:
- Using debugger (pdb/breakpoint)
- Adding logging for diagnosis
- Identifying common bugs
- Database best practices
- Error handling

Instructions:
1. Fix all the bugs marked with BUG comments
2. Run tests with: pytest test_problem2.py -v
"""

from flask import Flask, request, render_template_string, redirect
import sqlite3

app = Flask(__name__)


# BUG 1: Missing database initialization
def init_db():
    """
    Initialize the database.
    
    TODO: Create the notes table if it doesn't exist.
    Table should have: id (INTEGER PRIMARY KEY), title (TEXT), content (TEXT)
    """
    # TODO: Implement database initialization
    pass


# BUG 2: Database connection not closed (memory leak)
def get_db():
    """
    Get database connection.
    
    TODO: This function is missing proper connection management.
    Consider using context manager or ensuring connections are closed.
    """
    db = sqlite3.connect('notes.db')
    db.row_factory = sqlite3.Row
    return db


@app.route('/')
def index():
    """
    List all notes.
    
    BUG 2: Database connection not closed
    TODO: Fix memory leak by properly closing database connection
    """
    db = get_db()
    notes = db.execute('SELECT * FROM notes').fetchall()
    # BUG: Database connection not closed!
    
    template = """
    <html>
    <body>
        <h1>Notes</h1>
        <ul>
        {% for note in notes %}
            <li>{{ note['title'] }} - {{ note['content'] }}</li>
        {% endfor %}
        </ul>
        <form method="POST" action="/add">
            <input name="title" placeholder="Title" required>
            <input name="content" placeholder="Content" required>
            <button type="submit">Add Note</button>
        </form>
    </body>
    </html>
    """
    return render_template_string(template, notes=notes)


# BUG 3: SQL injection vulnerability
@app.route('/add', methods=['POST'])
def add_note():
    """
    Add a new note.
    
    BUG 3: SQL injection vulnerability
    TODO: Fix SQL injection by using parameterized queries
    
    BUG 2: Database connection not closed
    TODO: Ensure database connection is closed
    
    BUG 5: No error handling
    TODO: Add try-except error handling
    """
    title = request.form['title']
    content = request.form['content']
    db = get_db()
    
    # BUG: SQL injection vulnerability - string formatting in query!
    db.execute(f"INSERT INTO notes (title, content) VALUES ('{title}', '{content}')")
    db.commit()
    # BUG: Database connection not closed!
    
    return redirect('/')


# BUG 4: Wrong parameter type in tuple
@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    """
    Delete a note by ID.
    
    BUG 4: Wrong parameter type - missing comma in tuple
    TODO: Fix the tuple syntax in execute()
    
    BUG 2: Database connection not closed
    TODO: Ensure database connection is closed
    
    BUG 5: No error handling
    TODO: Add error handling for non-existent notes
    """
    db = get_db()
    
    # BUG: Missing trailing comma - (note_id) is not a tuple!
    db.execute('DELETE FROM notes WHERE id = ?', (note_id))
    db.commit()
    # BUG: Database connection not closed!
    
    return redirect('/')


@app.route('/search')
def search():
    """
    Search notes by title.
    
    BUG 5: No error handling
    TODO: Add error handling for missing query parameter
    
    BUG 2: Database connection not closed
    TODO: Ensure database connection is closed
    """
    query = request.args['q']  # BUG: No error handling if 'q' is missing!
    db = get_db()
    
    # Use parameterized query (this part is correct)
    notes = db.execute('SELECT * FROM notes WHERE title LIKE ?', (f'%{query}%',)).fetchall()
    # BUG: Database connection not closed!
    
    return f"Found {len(notes)} notes"


if __name__ == '__main__':
    init_db()
    # Debug mode is enabled for learning/development purposes only
    # Never use debug=True in production!
    app.run(debug=True)
