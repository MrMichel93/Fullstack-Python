"""
Practice Problem 2: URL Shortener with Click Tracking

Difficulty: Medium
Time: 30-40 minutes

Extend the basic URL shortener to track clicks:
- Add a clicks column to the database (default 0)
- Increment the click counter each time someone uses the short URL
- Create a statistics page (/stats/<short_code>) showing:
  - Original URL
  - Short URL
  - Total clicks
  - Creation date
- Display a list of all shortened URLs with their click counts

What you'll practice:
- UPDATE queries with incrementing
- Statistics display
- Data tables
- Multiple related pages

Instructions:
1. Complete the TODO sections below
2. Run tests with: pytest test_problem2.py -v
"""

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# TODO: Implement URL shortener with click tracking
# - Add clicks column to database
# - Increment clicks on each redirect
# - Create statistics page
# - List all URLs with click counts


if __name__ == '__main__':
    # Debug mode is enabled for learning/development purposes only
    # Never use debug=True in production!
    app.run(debug=True)
