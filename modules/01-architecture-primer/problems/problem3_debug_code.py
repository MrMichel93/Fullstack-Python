"""
Practice Problem 3: Debug the Architecture

Difficulty: Medium
Time: 15-20 minutes

A student built their first Flask app but things aren't working. Fix the bugs!

What you'll practice:
- Understanding HTTP methods in routes
- Safe parameter handling
- Template auto-escaping behavior

Instructions:
1. Fix all the bugs in the code below
2. Run tests with: pytest test_problem3.py -v
"""

from flask import Flask, request, render_template_string

app = Flask(__name__)


# BUG 1: Form submission not working
# Problem: "When I submit my form, nothing happens!"
@app.route('/contact')
def contact():
    """
    TODO: Fix this route so it can handle form submissions
    Hint: What HTTP method should forms use?
    """
    name = request.form.get('name', 'Guest')
    return f"Thanks, {name}!"


# BUG 2: KeyError when accessing page
# Problem: "I get a KeyError when accessing the page without parameters!"
@app.route('/profile')
def profile():
    """
    TODO: Fix this route to handle missing parameters gracefully
    Hint: What happens when username is not provided?
    """
    username = request.args['username']
    return f"Profile for {username}"


# BUG 3: HTML showing as text
# Problem: "My page shows <h1>Hello</h1> as text instead of a heading!"
@app.route('/welcome')
def welcome():
    """
    TODO: Fix this route so HTML is rendered properly
    Hint: Should the HTML be auto-escaped or marked as safe?
    """
    content = "<h1>Hello World</h1>"
    template = """
    <!DOCTYPE html>
    <html>
    <body>
        <div>{{ content }}</div>
    </body>
    </html>
    """
    return render_template_string(template, content=content)


# BUG 4: Wrong HTTP method
# Problem: "My delete button doesn't work!"
@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    """
    TODO: Fix this route to use the correct HTTP method for deletion
    Hint: DELETE or POST are safer than GET for destructive operations
    """
    # Simulate deletion
    return f"Item {item_id} deleted!"


# BUG 5: Missing error handling
# Problem: "App crashes when user enters invalid data!"
@app.route('/divide')
def divide():
    """
    TODO: Add error handling for missing or invalid parameters
    Hint: What if 'a' or 'b' are not provided? What if 'b' is zero?
    """
    a = float(request.args['a'])
    b = float(request.args['b'])
    result = a / b
    return f"Result: {result}"


if __name__ == '__main__':
    app.run(debug=True)
