"""
Practice Problem 3: Notes with Search

Difficulty: Hard
Time: 40-50 minutes

Add search functionality to your notes app:
- Add a search form on the home page
- Search notes by title and content (/notes/search?q=keyword)
- Highlight search terms in results
- Show "No results found" message when appropriate
- Display search results count
- Keep the search query in the search box after searching

What you'll practice:
- SQL LIKE queries for text search
- Working with query parameters
- Conditional rendering in templates
- User experience improvements

Instructions:
1. Complete the TODO sections below
2. Run tests with: pytest test_problem3.py -v
"""

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# TODO: Implement notes app with search functionality
# Add search form
# Support searching by title and content
# Display search results


if __name__ == '__main__':
    # Debug mode is enabled for learning/development purposes only
    # Never use debug=True in production!
    app.run(debug=True)
