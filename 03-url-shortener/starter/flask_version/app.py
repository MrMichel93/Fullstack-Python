"""
URL Shortener - Flask Version
A service to shorten long URLs and track clicks

Learning objectives:
- URL generation and routing
- HTTP redirects
- Click tracking
- Random string generation
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random
import string

app = Flask(__name__)
DATABASE = 'urls.db'


def get_db():
    """Create a database connection"""
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def init_db():
    """Initialize the database with urls table"""
    db = get_db()
    # TODO: Create the urls table
    # Table should have: id (INTEGER PRIMARY KEY), original_url (TEXT),
    # short_code (TEXT UNIQUE), clicks (INTEGER DEFAULT 0),
    # created_at (TIMESTAMP)
    # Hint: Use CREATE TABLE IF NOT EXISTS
    
    # Your code here:
    pass
    
    db.commit()
    db.close()


def generate_short_code(length=6):
    """Generate a random short code"""
    # TODO: Generate a random string of specified length
    # Use letters (a-z, A-Z) and digits (0-9)
    # Hint: string.ascii_letters + string.digits
    # Hint: random.choice() to pick random characters
    
    # Your code here:
    return "abc123"  # Replace with your generated code


@app.route('/')
def index():
    """Display the home page with URL shortening form"""
    return render_template('index.html', shortened_url=None)


@app.route('/shorten', methods=['POST'])
def shorten():
    """Handle URL shortening requests"""
    # TODO: Get the original URL from the form
    original_url = None  # Get from request.form
    
    # TODO: Validate the URL (basic check)
    # If empty, redirect back to home
    
    # TODO: Add http:// if not present
    # Hint: if not original_url.startswith(('http://', 'https://'))
    
    # TODO: Generate a unique short code
    # Keep trying until you get a unique one
    db = get_db()
    short_code = generate_short_code()
    
    # Check if code already exists (collision check)
    # while db.execute("SELECT id FROM urls WHERE short_code=?", (short_code,)).fetchone():
    #     short_code = generate_short_code()
    
    # TODO: Save to database
    # INSERT INTO urls (original_url, short_code) VALUES (?, ?)
    
    db.commit()
    db.close()
    
    # Create the full shortened URL
    shortened_url = url_for('redirect_to_url', short_code=short_code, _external=True)
    
    return render_template('index.html', shortened_url=shortened_url)


@app.route('/<short_code>')
def redirect_to_url(short_code):
    """Redirect short code to original URL and increment click counter"""
    db = get_db()
    
    # TODO: Look up the short code in the database
    # Hint: SELECT * FROM urls WHERE short_code = ?
    url_data = None  # Replace with your query
    
    if url_data is None:
        db.close()
        return "URL not found", 404
    
    # TODO: Increment the click counter
    # Hint: UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?
    
    db.commit()
    db.close()
    
    # TODO: Redirect to the original URL
    # Hint: redirect(url_data['original_url'], code=301)
    return redirect('/')  # Replace with actual redirect


@app.route('/stats')
def stats():
    """Display statistics for all shortened URLs"""
    db = get_db()
    
    # TODO: Fetch all URLs with their statistics
    # Hint: SELECT * FROM urls ORDER BY clicks DESC
    urls = []  # Replace with your query
    
    db.close()
    return render_template('stats.html', urls=urls)


if __name__ == '__main__':
    init_db()
    print("🔗 URL Shortener is running!")
    print("📊 Open http://localhost:5000 in your browser")
    print("📈 View stats at http://localhost:5000/stats")
    app.run(debug=True, port=5000)
