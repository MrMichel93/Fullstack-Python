"""
Practice Problem 2: Inventory Tracker

Instructions:
1. Complete the TODO sections below
2. Run tests with: pytest test_problem2.py -v
"""

from flask import Flask, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'dev-secret-key'

# TODO: Implement authentication and inventory system

if __name__ == '__main__':
    app.run(debug=True)
