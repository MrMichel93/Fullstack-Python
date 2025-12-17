"""
Practice Problem 3: Simple Form Handler

Difficulty: Medium
Time: 20-30 minutes

Create a Flask application with a feedback form:
- A page with a form that accepts: name, email, and message
- Form should submit to /submit using POST method
- After submission, redirect to a thank you page (/thank-you)
- Display a flash message on the thank you page: "Thank you [name], we received your message!"
- If any field is empty, show an error flash message and redisplay the form
- Style is optional but tests focus on functionality

What you'll practice:
- HTML forms with POST method
- Getting form data with request.form
- Redirects with redirect() and url_for()
- Flash messages for user feedback
- Basic form validation

Bonus Challenge:
- Save submitted feedback to a list (stored in memory)
- Create a /feedback route that displays all submitted feedback

Instructions:
1. Complete the TODO sections below
2. Run tests with: pytest test_problem3.py -v
"""

from flask import Flask, render_template_string, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# In-memory storage for feedback (bonus feature)
feedback_list = []


# TODO: Create route for the form page (GET /)
# Should display a form with fields: name, email, message
# Form should POST to /submit


# TODO: Create route for form submission (POST /submit)
# - Validate that name, email, and message are not empty
# - If validation fails, flash error message and redirect back to form
# - If validation passes:
#   - Flash success message with the name
#   - Optionally save to feedback_list
#   - Redirect to /thank-you


# TODO: Create route for thank you page (GET /thank-you)
# Should display the flash message(s)


# BONUS TODO: Create route to display all feedback (GET /feedback)
# Should display all submitted feedback from feedback_list


if __name__ == '__main__':
    # Debug mode is enabled for learning/development purposes only
    # Never use debug=True in production!
    app.run(debug=True)
