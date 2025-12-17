"""
Practice Problem 2: Prevent Security Vulnerabilities

Difficulty: Medium
Time: 20-25 minutes

Fix security vulnerabilities in the provided Flask code.

⚠️ WARNING: This code contains intentional vulnerabilities for educational purposes!
Never use this code in production!

What you'll practice:
- Preventing XSS attacks
- Preventing SQL injection
- Safe parameter handling

Instructions:
1. Fix all the security vulnerabilities marked with TODO
2. Run tests with: pytest test_problem2.py -v
"""

from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)


def get_db():
    """Get database connection."""
    db = sqlite3.connect(':memory:')
    db.row_factory = sqlite3.Row
    # Create test table
    db.execute('''CREATE TABLE IF NOT EXISTS users 
                  (id INTEGER PRIMARY KEY, username TEXT, email TEXT)''')
    db.execute("INSERT INTO users (username, email) VALUES ('alice', 'alice@example.com')")
    db.execute("INSERT INTO users (username, email) VALUES ('bob', 'bob@example.com')")
    db.commit()
    return db


# VULNERABILITY 1: XSS (Cross-Site Scripting)
# Problem: User input is displayed without escaping
@app.route('/search')
def search():
    """
    TODO: Fix the XSS vulnerability
    
    Current problem: The search query is directly inserted into HTML
    without escaping, allowing script injection.
    
    Fix options:
    1. Use render_template_string with auto-escaping
    2. Use Markup with proper escaping
    3. Validate and sanitize input
    """
    query = request.args.get('q', '')
    # VULNERABLE: Direct string concatenation with user input
    return f"<h1>Search results for: {query}</h1>"


# VULNERABILITY 2: SQL Injection
# Problem: User input is directly inserted into SQL query
@app.route('/user/<username>')
def user_profile(username):
    """
    TODO: Fix the SQL injection vulnerability
    
    Current problem: Username is directly inserted into SQL query
    using string formatting, allowing SQL injection.
    
    Fix: Use parameterized queries with ? placeholders
    """
    db = get_db()
    # VULNERABLE: String formatting in SQL query
    sql = f"SELECT * FROM users WHERE username = '{username}'"
    cursor = db.execute(sql)
    user = cursor.fetchone()
    db.close()
    
    if user:
        return f"User: {user['username']}, Email: {user['email']}"
    return "User not found", 404


# VULNERABILITY 3: Missing Input Validation
# Problem: No validation on user input
@app.route('/api/user/<int:user_id>')
def get_user_api(user_id):
    """
    TODO: Add input validation
    
    Current problem: No validation on user_id range or existence
    
    Fix: Validate that user_id is positive and handle missing users
    """
    db = get_db()
    # Missing validation - what if user_id is negative or doesn't exist?
    cursor = db.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    db.close()
    
    # TODO: Add proper validation and error handling
    return f"User: {user['username']}"


# VULNERABILITY 4: Unsafe HTML Rendering
# Problem: User content rendered without escaping
@app.route('/comment', methods=['POST'])
def post_comment():
    """
    TODO: Fix unsafe HTML rendering
    
    Current problem: User comments are rendered as raw HTML
    
    Fix: Properly escape user content in template
    """
    comment = request.form.get('comment', '')
    
    # VULNERABLE: Using |safe filter on user input
    template = """
    <html>
    <body>
        <h2>Your comment:</h2>
        <div>{{ comment|safe }}</div>
    </body>
    </html>
    """
    return render_template_string(template, comment=comment)


if __name__ == '__main__':
    app.run(debug=True)
