"""
Practice Problem 3: Simple Blog

Instructions:
1. Complete the TODO sections below
2. Run tests with: pytest test_problem3.py -v
"""

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# TODO: Implement blog application

if __name__ == '__main__':
    # Debug mode is enabled for learning/development purposes only
    # Never use debug=True in production!
    app.run(debug=True)
