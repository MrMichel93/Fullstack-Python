"""
Practice Problem 1: Personal Portfolio Page

Difficulty: Easy
Time: 15-20 minutes

Create a Flask application with the following features:
- A home page (/) that displays your name and a welcome message
- An about page (/about) that shows information about you
- A contact page (/contact) that displays your email
- Use template inheritance with a base.html template
- Add a navigation bar that works on all pages

What you'll practice:
- Creating multiple routes
- Using templates and template inheritance
- Using url_for() for navigation

Instructions:
1. Complete the TODO sections below
2. Create the required templates in a 'templates' directory
3. Run tests with: pytest test_problem1.py -v
"""

from flask import Flask, render_template

app = Flask(__name__)

# TODO: Create route for home page (/)
# Should render 'home.html' template


# TODO: Create route for about page (/about)
# Should render 'about.html' template


# TODO: Create route for contact page (/contact)
# Should render 'contact.html' template


if __name__ == '__main__':
    # Debug mode is enabled for learning/development purposes only
    # Never use debug=True in production!
    app.run(debug=True)
