"""
Practice Problem 3: URL Shortener with Copy Feature

Difficulty: Medium
Time: 30-40 minutes

Add frontend features to your URL shortener:
- Add a "Copy to Clipboard" button next to the shortened URL
- Use JavaScript to implement the copy functionality
- Show a "Copied!" message after successful copy
- Add URL validation to reject invalid URLs
- Style the application with CSS for better UX

What you'll practice:
- JavaScript clipboard API
- URL validation
- User feedback mechanisms
- Frontend/backend integration

Instructions:
1. Complete the TODO sections below
2. Run tests with: pytest test_problem3.py -v
"""

from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# TODO: Implement URL shortener with copy feature
# - Add URL validation
# - Create result page with copy button
# - Implement JavaScript for clipboard
# - Add CSS styling


if __name__ == '__main__':
    app.run(debug=True)
