"""
URL Shortener - Flask Version (Complete Solution)
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
    db.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL,
            clicks INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.commit()
    db.close()


def generate_short_code(length=6):
    """Generate a random short code"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


@app.route('/')
def index():
    """Display the home page with URL shortening form"""
    return render_template('index.html', shortened_url=None)


@app.route('/shorten', methods=['POST'])
def shorten():
    """Handle URL shortening requests"""
    original_url = request.form.get('original_url', '').strip()
    
    if not original_url:
        return redirect(url_for('index'))
    
    # Add http:// if not present
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'https://' + original_url
    
    db = get_db()
    
    # Generate unique short code
    short_code = generate_short_code()
    while db.execute("SELECT id FROM urls WHERE short_code=?", (short_code,)).fetchone():
        short_code = generate_short_code()
    
    # Save to database
    db.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)',
               (original_url, short_code))
    db.commit()
    db.close()
    
    # Create the full shortened URL
    shortened_url = url_for('redirect_to_url', short_code=short_code, _external=True)
    
    return render_template('index.html', shortened_url=shortened_url)


@app.route('/<short_code>')
def redirect_to_url(short_code):
    """Redirect short code to original URL and increment click counter"""
    db = get_db()
    url_data = db.execute('SELECT * FROM urls WHERE short_code = ?', (short_code,)).fetchone()
    
    if url_data is None:
        db.close()
        return "URL not found", 404
    
    # Increment click counter
    db.execute('UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?', (short_code,))
    db.commit()
    db.close()
    
    return redirect(url_data['original_url'], code=301)


@app.route('/stats')
def stats():
    """Display statistics for all shortened URLs"""
    db = get_db()
    urls = db.execute('SELECT * FROM urls ORDER BY clicks DESC').fetchall()
    db.close()
    return render_template('stats.html', urls=urls)


if __name__ == '__main__':
    init_db()
    print("🔗 URL Shortener is running!")
    print("📊 Open http://localhost:5000 in your browser")
    print("📈 View stats at http://localhost:5000/stats")
    # NOTE: debug=True is for development/learning only
    # In production, set debug=False and use a proper WSGI server
    app.run(debug=True, port=5000)
