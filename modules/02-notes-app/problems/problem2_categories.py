"""
Practice Problem 2: Notes with Categories

Difficulty: Medium
Time: 30-40 minutes

Extend the basic notes app to support categories:
- Add a category field to the notes table (e.g., "Work", "Personal", "Ideas")
- Display notes grouped by category on the home page
- Add a filter to show notes from a specific category (/notes?category=Work)
- Show a category dropdown in the create/edit forms
- Display a count of notes in each category

What you'll practice:
- More complex SQL queries with WHERE clauses
- URL query parameters with request.args
- Grouping and filtering data
- Working with multiple database fields

Instructions:
1. Complete the TODO sections below
2. Run tests with: pytest test_problem2.py -v
"""

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# TODO: Implement notes app with categories
# Add category field to database
# Support filtering by category
# Show category in note display


if __name__ == '__main__':
    # Debug mode is enabled for learning/development purposes only
    # Never use debug=True in production!
    app.run(debug=True)
