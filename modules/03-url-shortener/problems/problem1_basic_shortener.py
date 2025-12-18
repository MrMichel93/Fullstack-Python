"""
Practice Problem 1: Basic URL Shortener

Difficulty: Medium
Time: 30-40 minutes

Create a Flask application that shortens URLs:
- Home page with a form to submit long URLs
- Generate a 6-character random short code
- Store short code and long URL in SQLite database
- Display the shortened URL after submission
- Redirect users when they visit the short URL (/<short_code>)
- Show "404 Not Found" for invalid short codes

What you'll practice:
- Random string generation
- Database INSERT and SELECT
- HTTP redirects (302)
- Dynamic routing with parameters

Instructions:
1. Complete the TODO sections below
2. Run tests with: pytest test_problem1.py -v
"""

from flask import Flask, request, redirect, url_for
import sqlite3
import string
import random

app = Flask(__name__)

# TODO: Implement URL shortener
# - Create database with urls table (id, short_code, long_url, created_at)
# - Generate random 6-character codes
# - Store URLs in database
# - Redirect short codes to original URLs


if __name__ == '__main__':
    app.run(debug=True)
