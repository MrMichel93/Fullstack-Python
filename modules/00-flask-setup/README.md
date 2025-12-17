# Flask Setup & Installation Guide

## What You'll Learn
- How to install Flask
- Understanding Flask basics
- Setting up your development environment
- Creating your first Flask application
- Flask project structure

---

## 1. Installing Flask

### Prerequisites
Before installing Flask, ensure you have:
- Python 3.8 or higher
- pip (Python package manager)
- A text editor or IDE (VS Code, PyCharm, etc.)

### Step 1: Create a Project Directory
```bash
mkdir my-flask-app
cd my-flask-app
```

### Step 2: Create a Virtual Environment
A virtual environment keeps your project dependencies isolated.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You'll see `(venv)` in your terminal when activated.

### Step 3: Install Flask
```bash
pip install Flask
```

### Step 4: Verify Installation
```bash
python -c "import flask; print(flask.__version__)"
```

You should see the Flask version number (e.g., `3.0.0`).

---

## 2. Understanding Flask

### What is Flask?
Flask is a **lightweight web framework** for Python that makes it easy to build web applications.

**Key Features:**
- **Minimal** - Only includes essentials, you add what you need
- **Flexible** - Choose your own tools and libraries
- **Easy to Learn** - Simple API and clear documentation
- **Built-in Development Server** - Test your app locally
- **Template Engine (Jinja2)** - Generate dynamic HTML

### Flask vs Other Frameworks
- **Flask** - Lightweight, flexible, "micro" framework
- **Django** - Full-featured, "batteries included" framework
- **FastAPI** - Modern, fast, API-focused framework

**Why Flask for this course?**
- Easier for beginners
- Clear and simple structure
- Great for learning web fundamentals
- Widely used in industry

---

## 3. Your First Flask Application

### Create app.py
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Flask!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
```

### Understanding the Code

**Line 1: Import Flask**
```python
from flask import Flask
```
Imports the Flask class from the flask package.

**Line 3: Create Flask Application**
```python
app = Flask(__name__)
```
Creates an instance of the Flask application. `__name__` helps Flask locate resources.

**Line 5-7: Define a Route**
```python
@app.route('/')
def home():
    return "<h1>Hello, Flask!</h1>"
```
- `@app.route('/')` - Decorator that maps URL `/` to the function
- `def home()` - Function that handles requests to `/`
- `return` - Sends HTML back to the browser

**Line 9-10: Run the Application**
```python
if __name__ == '__main__':
    app.run(debug=True)
```
- Starts the development server
- `debug=True` enables auto-reload and detailed error messages

### Run Your Application
```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Restarting with stat
 * Debugger is active!
```

Open your browser and visit `http://localhost:5000` - you'll see "Hello, Flask!"

---

## 4. Flask Project Structure

### Basic Structure
```
my-flask-app/
├── venv/                 # Virtual environment (don't commit to git)
├── app.py                # Main application file
├── requirements.txt      # List of dependencies
└── .gitignore           # Files to ignore in git
```

### Full Structure (for larger projects)
```
my-flask-app/
├── venv/
├── app.py
├── requirements.txt
├── .gitignore
├── static/              # CSS, JavaScript, images
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── templates/           # HTML templates
│   ├── base.html
│   ├── index.html
│   └── about.html
└── database.db          # SQLite database (auto-generated)
```

### Key Directories

**static/**
- Store CSS, JavaScript, and image files
- Accessed directly by the browser
- Example: `/static/css/style.css`

**templates/**
- HTML templates with Jinja2 syntax
- Rendered by Flask with dynamic data
- Example: `render_template('index.html')`

---

## 5. Flask Basics

### Routes and URL Patterns

**Simple Route**
```python
@app.route('/')
def home():
    return "Home Page"
```

**Route with Parameter**
```python
@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"
```

**Multiple Routes for Same Function**
```python
@app.route('/')
@app.route('/home')
def home():
    return "Home Page"
```

**Route with HTTP Methods**
```python
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return "Form submitted!"
    return "Show form"
```

### Templates (Jinja2)

**Create templates/index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ message }}</p>
</body>
</html>
```

**Render Template in app.py**
```python
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html',
                         title='Home',
                         heading='Welcome!',
                         message='This is Flask')
```

### Static Files

**Link CSS in Template**
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

**Link JavaScript**
```html
<script src="{{ url_for('static', filename='js/main.js') }}"></script>
```

**Link Images**
```html
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
```

### Request Data

**Get Form Data**
```python
from flask import request

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return f"Logging in as {username}"
```

**Get URL Parameters**
```python
@app.route('/search')
def search():
    query = request.args.get('q', '')  # /search?q=flask
    return f"Searching for: {query}"
```

### Redirects
```python
from flask import redirect, url_for

@app.route('/old-page')
def old_page():
    return redirect(url_for('new_page'))

@app.route('/new-page')
def new_page():
    return "This is the new page"
```

---

## 6. Common Flask Patterns

### Flash Messages (User Feedback)
```python
from flask import flash, redirect, url_for

@app.route('/save', methods=['POST'])
def save():
    # Process data
    flash('Data saved successfully!', 'success')
    return redirect(url_for('home'))
```

**Display in Template**
```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }}">{{ message }}</div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

### Error Handling
```python
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500
```

### Template Inheritance

**Base Template (base.html)**
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My App{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>© 2024 My App</footer>
</body>
</html>
```

**Child Template (index.html)**
```html
{% extends "base.html" %}

{% block title %}Home - My App{% endblock %}

{% block content %}
    <h1>Welcome to My App</h1>
    <p>This is the home page.</p>
{% endblock %}
```

---

## 7. Development Best Practices

### Use Debug Mode During Development
```python
app.run(debug=True)
```
**Benefits:**
- Auto-reloads when code changes
- Shows detailed error pages
- Interactive debugger

**WARNING:** Never use `debug=True` in production!

### Create requirements.txt
List all dependencies:
```bash
pip freeze > requirements.txt
```

Install from requirements.txt:
```bash
pip install -r requirements.txt
```

### Use .gitignore
Create `.gitignore` file:
```
venv/
__pycache__/
*.pyc
*.db
.env
.DS_Store
```

### Environment Variables
Store sensitive data in environment variables:

**Create .env file**
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///database.db
```

**Load in app.py**
```python
import os
from dotenv import load_dotenv

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
```

---

## 8. Running Flask Applications

### Development Mode
```bash
python app.py
```

### Using Flask CLI
```bash
export FLASK_APP=app.py      # On Linux/Mac
set FLASK_APP=app.py         # On Windows
flask run
```

### Custom Host and Port
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

### Access from Other Devices
```python
# Run on all network interfaces
app.run(host='0.0.0.0', debug=True)
```
Now accessible at `http://your-ip-address:5000`

---

## 9. Quick Reference

### Essential Flask Imports
```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
```

### Common Flask Patterns
```python
# Create app
app = Flask(__name__)

# Route
@app.route('/path')
def function_name():
    return "response"

# Render template
return render_template('template.html', variable=value)

# Redirect
return redirect(url_for('function_name'))

# Get form data
data = request.form['field_name']

# Get URL parameters
param = request.args.get('param_name')

# Run app
if __name__ == '__main__':
    app.run(debug=True)
```

---

## 10. Practice Problems

Ready to practice what you've learned? Complete the **[Practice Problems](./practice-problems.md)** to solidify your Flask knowledge!

**What you'll build:**
- Personal portfolio page with multiple routes
- Dynamic greeting app with URL parameters
- Form handler with validation and flash messages

These exercises are designed to reinforce the concepts from this module.

---

## 11. Next Steps

Now that you understand Flask basics:

1. ✅ Flask is installed
2. ✅ You understand the project structure
3. ✅ You can create routes and templates
4. ✅ You know how to run Flask apps

**Continue to:** [Architecture Primer](../01-architecture-primer/) to understand web fundamentals before building projects.

---

## 12. Resources

### Official Documentation
- Flask Docs: https://flask.palletsprojects.com/
- Jinja2 Templates: https://jinja.palletsprojects.com/

### Tutorials
- Flask Quickstart: https://flask.palletsprojects.com/quickstart/
- Flask Mega-Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

### Tools
- Flask Extensions: https://flask.palletsprojects.com/extensions/
- Flask Debug Toolbar: https://flask-debugtoolbar.readthedocs.io/

---

**Ready to learn web architecture?** Head to [Architecture Primer](../01-architecture-primer/)!
