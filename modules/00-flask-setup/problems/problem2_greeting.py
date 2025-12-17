"""
Practice Problem 2: Dynamic Greeting App

Difficulty: Easy
Time: 15-20 minutes

Create a Flask application that:
- Has a route /greet/<name> that displays a personalized greeting
- Has a route /greet (without name) that shows a default greeting
- Has a route /greet with query parameter ?name=<name>&time=<morning|afternoon|evening>
  that shows time-specific greetings
- Displays different greetings based on the time parameter
  (e.g., "Good morning, Alice!")

What you'll practice:
- Routes with parameters
- URL query parameters with request.args
- Conditional logic in templates or routes

Instructions:
1. Complete the TODO sections below
2. Run tests with: pytest test_problem2.py -v
"""

from flask import Flask, request

app = Flask(__name__)


# TODO: Create route /greet (no parameter)
# Should return a default greeting like "Hello, Guest!"


# TODO: Create route /greet/<name>
# Should return a personalized greeting like "Hello, {name}!"


# TODO: Create route /greet/time that accepts query parameters
# ?name=<name>&time=<morning|afternoon|evening>
# Should return time-specific greeting like:
# - "Good morning, {name}!"
# - "Good afternoon, {name}!"
# - "Good evening, {name}!"
# If name is not provided, use "Guest"
# If time is not provided or invalid, use "Hello"


if __name__ == '__main__':
    app.run(debug=True)
