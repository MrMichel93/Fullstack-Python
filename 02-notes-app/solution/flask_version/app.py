"""
Notes App - Flask Version (Complete Solution)
A simple CRUD application for managing notes
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'notes.db'


def get_db():
    """Create a database connection"""
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def init_db():
    """Initialize the database with notes table"""
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


@app.route('/')
def index():
    """Display all notes on the home page"""
    db = get_db()
    notes = db.execute('SELECT * FROM notes ORDER BY created_at DESC').fetchall()
    db.close()
    return render_template('index.html', notes=notes)


@app.route('/notes', methods=['POST'])
def create_note():
    """Handle creating a new note"""
    title = request.form['title']
    content = request.form['content']
    
    # Basic validation
    if not title or not content:
        return redirect(url_for('index'))
    
    db = get_db()
    db.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
    db.commit()
    db.close()
    
    return redirect(url_for('index'))


@app.route('/notes/<int:note_id>/edit')
def edit_note(note_id):
    """Display the edit form for a specific note"""
    db = get_db()
    note = db.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()
    db.close()
    
    if note is None:
        return "Note not found", 404
    
    return render_template('edit.html', note=note)


@app.route('/notes/<int:note_id>/update', methods=['POST'])
def update_note(note_id):
    """Handle updating an existing note"""
    title = request.form['title']
    content = request.form['content']
    
    db = get_db()
    db.execute('UPDATE notes SET title=?, content=? WHERE id=?',
               (title, content, note_id))
    db.commit()
    db.close()
    
    return redirect(url_for('index'))


@app.route('/notes/<int:note_id>/delete', methods=['POST'])
def delete_note(note_id):
    """Handle deleting a note"""
    db = get_db()
    db.execute('DELETE FROM notes WHERE id=?', (note_id,))
    db.commit()
    db.close()
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    print("🚀 Notes App is running!")
    print("📝 Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
