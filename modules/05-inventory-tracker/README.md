# Inventory Tracker - User Authentication & Sessions

## What You'll Learn
- User authentication (register, login, logout)
- Password hashing with Werkzeug
- Session management
- Protected routes (decorators)
- User-specific data isolation
- Login/registration forms
- Flash messages for user feedback
- Protected page patterns
- Dashboard layouts

---

## 1. User Authentication Overview

### What is Authentication?

**Authentication** is the process of verifying who a user is:
- **Registration** - Creating a new user account
- **Login** - Verifying user credentials
- **Logout** - Ending the user session
- **Session** - Maintaining user state across requests

**Why Authentication Matters:**
- Protect sensitive data
- Personalize user experience
- Track user actions
- Control access to features

---

## 2. Password Hashing

### Never Store Plain Text Passwords!

**BAD - NEVER DO THIS:**
```python
# INSECURE! Don't store passwords as plain text
password = request.form['password']
db.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
           (username, password))
```

**GOOD - Hash Passwords:**
```python
from werkzeug.security import generate_password_hash, check_password_hash

# Register - hash the password
password = request.form['password']
hashed_password = generate_password_hash(password)
db.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
           (username, hashed_password))

# Login - verify the password
stored_hash = db.execute('SELECT password FROM users WHERE username = ?', 
                         (username,)).fetchone()['password']
if check_password_hash(stored_hash, password):
    # Password is correct!
    pass
```

### How Password Hashing Works

```python
# Hashing is one-way
password = "mypassword123"
hashed = generate_password_hash(password)
print(hashed)  
# Output: pbkdf2:sha256:260000$salt$hash...

# You can't reverse the hash
# But you can verify if a password matches
check_password_hash(hashed, "mypassword123")  # True
check_password_hash(hashed, "wrongpassword")  # False
```

---

## 3. Session Management

### What are Sessions?

**Sessions** allow you to store data about a user across requests:
- Flask uses cookies to store a session ID
- Session data is stored server-side
- Cookies are encrypted with a secret key

### Using Flask Sessions

```python
from flask import session

app.secret_key = 'your-secret-key-here'  # Required for sessions

# Login - store user in session
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Verify credentials
    user = db.execute('SELECT * FROM users WHERE username = ?', 
                     (username,)).fetchone()
    
    if user and check_password_hash(user['password'], password):
        # Store user ID in session
        session['user_id'] = user['id']
        session['username'] = user['username']
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    
    flash('Invalid credentials', 'error')
    return redirect(url_for('login'))

# Logout - clear session
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('home'))

# Check if user is logged in
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login first', 'error')
        return redirect(url_for('login'))
    
    return render_template('dashboard.html')
```

---

## 4. Protected Routes with Decorators

### Creating a Login Required Decorator

```python
from functools import wraps

def login_required(f):
    """Decorator to require login for routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Usage
@app.route('/dashboard')
@login_required
def dashboard():
    # This route requires login
    return render_template('dashboard.html')

@app.route('/profile')
@login_required
def profile():
    # This route also requires login
    user_id = session['user_id']
    user = get_user(user_id)
    return render_template('profile.html', user=user)
```

---

## 5. User Registration

### Registration Form

```html
<!-- register.html -->
<h1>Register</h1>

<form method="POST" action="/register">
    <div>
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
    </div>
    
    <div>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
    </div>
    
    <div>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
    </div>
    
    <div>
        <label for="confirm">Confirm Password:</label>
        <input type="password" id="confirm" name="confirm" required>
    </div>
    
    <button type="submit">Register</button>
</form>

<p>Already have an account? <a href="/login">Login</a></p>
```

### Registration Route

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm']
        
        # Validate input
        if not username or not email or not password:
            flash('All fields are required', 'error')
            return redirect(url_for('register'))
        
        if password != confirm:
            flash('Passwords do not match', 'error')
            return redirect(url_for('register'))
        
        # Check if username exists
        db = get_db()
        existing = db.execute('SELECT id FROM users WHERE username = ?', 
                            (username,)).fetchone()
        
        if existing:
            flash('Username already exists', 'error')
            db.close()
            return redirect(url_for('register'))
        
        # Create user
        hashed_password = generate_password_hash(password)
        db.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                  (username, email, hashed_password))
        db.commit()
        db.close()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')
```

---

## 6. User-Specific Data

### Isolating Data by User

```python
# Get only the current user's items
@app.route('/items')
@login_required
def list_items():
    user_id = session['user_id']
    
    db = get_db()
    items = db.execute(
        'SELECT * FROM items WHERE user_id = ? ORDER BY created_at DESC',
        (user_id,)
    ).fetchall()
    db.close()
    
    return render_template('items.html', items=items)

# Create item for current user
@app.route('/items/create', methods=['POST'])
@login_required
def create_item():
    user_id = session['user_id']
    name = request.form['name']
    quantity = request.form['quantity']
    
    db = get_db()
    db.execute(
        'INSERT INTO items (user_id, name, quantity) VALUES (?, ?, ?)',
        (user_id, name, quantity)
    )
    db.commit()
    db.close()
    
    flash('Item added!', 'success')
    return redirect(url_for('list_items'))
```

---

## 7. Flash Messages

### Displaying User Feedback

```python
from flask import flash

# Set flash messages
flash('Login successful!', 'success')
flash('Invalid password', 'error')
flash('Profile updated', 'info')
flash('Are you sure?', 'warning')
```

```html
<!-- Display flash messages in template -->
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        <div class="flash-messages">
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">
                    {{ message }}
                    <button class="close" onclick="this.parentElement.remove()">×</button>
                </div>
            {% endfor %}
        </div>
    {% endif %}
{% endwith %}
```

```css
/* Style flash messages */
.alert {
    padding: 1rem;
    margin-bottom: 1rem;
    border-radius: 4px;
}

.alert-success {
    background-color: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

.alert-error {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}
```

---

## 8. Dashboard Layout

### User Dashboard

```html
<!-- dashboard.html -->
{% extends "base.html" %}

{% block content %}
<div class="dashboard">
    <aside class="sidebar">
        <h2>Welcome, {{ session.username }}!</h2>
        <nav>
            <a href="/dashboard">Dashboard</a>
            <a href="/items">My Items</a>
            <a href="/profile">Profile</a>
            <a href="/logout">Logout</a>
        </nav>
    </aside>
    
    <main class="dashboard-content">
        <h1>Dashboard</h1>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>Total Items</h3>
                <p class="big-number">{{ total_items }}</p>
            </div>
            
            <div class="stat-card">
                <h3>Low Stock</h3>
                <p class="big-number">{{ low_stock_count }}</p>
            </div>
        </div>
        
        <div class="recent-activity">
            <h2>Recent Activity</h2>
            <!-- Recent items -->
        </div>
    </main>
</div>
{% endblock %}
```

---

## 9. Security Best Practices

### Secure Session Configuration

```python
import os

app.secret_key = os.environ.get('SECRET_KEY') or 'dev-secret-key'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# In production, also use:
# app.config['SESSION_COOKIE_SECURE'] = True  # HTTPS only
```

### Input Validation

```python
def validate_password(password):
    """Validate password strength."""
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    if not any(c.isupper() for c in password):
        return False, "Password must contain uppercase letter"
    if not any(c.isdigit() for c in password):
        return False, "Password must contain a number"
    return True, "Password is valid"

# Usage
is_valid, message = validate_password(password)
if not is_valid:
    flash(message, 'error')
    return redirect(url_for('register'))
```

---

## 10. Practice Problems

Ready to implement authentication? Complete the **[Practice Problems](./practice-problems.md)** to build secure user systems!

**What you'll build:**
- User registration and login
- Protected inventory system
- User-specific data
- Session management
- Secure password handling

---

## 11. Quick Reference

### Password Hashing
```python
from werkzeug.security import generate_password_hash, check_password_hash

# Hash
hashed = generate_password_hash(password)

# Verify
if check_password_hash(hashed, password):
    # Correct!
```

### Sessions
```python
# Store
session['user_id'] = user.id

# Retrieve
user_id = session.get('user_id')

# Clear
session.clear()
```

### Login Required Decorator
```python
@login_required
def protected_route():
    user_id = session['user_id']
```

---

## 12. Next Steps

After completing this module:

1. ✅ You can implement user authentication
2. ✅ You understand password security
3. ✅ You can manage sessions
4. ✅ You can protect routes

**Continue to:** [Security Basics](../06-security-basics/) and [Debugging & Testing](../07-debugging-testing/)

---

**Ready to build secure applications?** Head to [Practice Problems](./practice-problems.md)!
