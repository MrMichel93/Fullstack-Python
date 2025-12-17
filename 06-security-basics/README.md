# Security Basics

## 🔒 Why Security Matters

Security isn't optional—it's essential. Even simple projects can have vulnerabilities that expose user data or allow attackers to compromise your application.

**This guide covers:**
1. Password hashing and authentication
2. Input validation and sanitization
3. Common web vulnerabilities
4. Security best practices

---

## 1. Password Hashing

### ❌ NEVER Store Plain Text Passwords

**Bad (Never do this):**
```python
# INSECURE - Don't do this!
password = request.form['password']
db.execute("INSERT INTO users (username, password) VALUES (?, ?)",
           (username, password))
```

**Why it's bad:**
- If database is compromised, all passwords are exposed
- Employees/admins can see user passwords
- Users often reuse passwords across sites

### ✅ Use Password Hashing

**Good (Always do this):**
```python
from werkzeug.security import generate_password_hash, check_password_hash

# When creating account
password = request.form['password']
hashed = generate_password_hash(password)
db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
           (username, hashed))

# When logging in
user = db.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
if user and check_password_hash(user['password_hash'], password):
    # Login successful
    pass
```

### How It Works

```
User Password: "mypassword123"
         ↓
   Hash Function (bcrypt, pbkdf2, etc.)
         ↓
Stored Hash: "$2b$12$KIXn7..."  ← Stored in database
```

**Key Points:**
- **One-way:** Can't reverse hash to get password
- **Unique:** Same password + different salt = different hash
- **Slow:** Intentionally slow to prevent brute force attacks
- **Salt:** Random data added to prevent rainbow table attacks

### Password Requirements

```python
def validate_password(password):
    """Check password meets minimum requirements"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters"
    
    if not any(c.isupper() for c in password):
        return False, "Password must contain uppercase letter"
    
    if not any(c.isdigit() for c in password):
        return False, "Password must contain a number"
    
    return True, "Password is valid"
```

---

## 2. Input Validation & Sanitization

### Always Validate User Input

**Never trust data from:**
- Form submissions
- URL parameters
- Cookies
- File uploads
- HTTP headers

### Example: Email Validation

```python
import re

def is_valid_email(email):
    """Basic email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# In your route
email = request.form.get('email', '').strip()
if not is_valid_email(email):
    return "Invalid email address", 400
```

### Sanitize HTML Input

```python
import html

# Escape HTML special characters
user_input = request.form['comment']
safe_input = html.escape(user_input)

# <script>alert('xss')</script>  becomes:
# &lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;
```

### Whitelist > Blacklist

**Bad approach:**
```python
# Trying to block bad inputs (incomplete)
if '<script>' in user_input or 'DROP TABLE' in user_input:
    return "Invalid input"
```

**Good approach:**
```python
# Only allow known-good inputs
ALLOWED_CATEGORIES = ['tech', 'sports', 'news', 'entertainment']
category = request.form['category']
if category not in ALLOWED_CATEGORIES:
    return "Invalid category", 400
```

---

## 3. Common Web Vulnerabilities

### SQL Injection

**Vulnerable Code:**
```python
# ❌ NEVER DO THIS
username = request.form['username']
query = f"SELECT * FROM users WHERE username = '{username}'"
db.execute(query)

# Attacker enters: ' OR '1'='1
# Resulting query: SELECT * FROM users WHERE username = '' OR '1'='1'
# Returns ALL users!
```

**Secure Code:**
```python
# ✅ Use parameterized queries
username = request.form['username']
db.execute("SELECT * FROM users WHERE username = ?", (username,))
# The ? placeholder safely escapes the input
```

**Key Points:**
- Always use parameterized queries (?, ?)
- Never concatenate user input into SQL
- ORM frameworks (SQLAlchemy) handle this automatically

### Cross-Site Scripting (XSS)

**Vulnerable Code:**
```python
# ❌ Rendering user input directly
comment = request.form['comment']
return f"<p>You said: {comment}</p>"

# Attacker enters: <script>steal_cookies()</script>
# Browser executes the malicious script!
```

**Secure Code:**
```python
# ✅ Templates auto-escape by default
return render_template('comment.html', comment=comment)

# In template (Jinja2 auto-escapes):
<p>You said: {{ comment }}</p>

# <script> tags are rendered as text, not executed
```

**Key Points:**
- Use template engines (Jinja2, Django templates)
- They automatically escape HTML
- Only use `|safe` filter when absolutely necessary
- Sanitize HTML if users need formatting (use libraries like Bleach)

### Cross-Site Request Forgery (CSRF)

**What is CSRF?**
Attacker tricks victim into submitting a malicious request.

**Example Attack:**
```html
<!-- Malicious site tricks logged-in user -->
<img src="https://yourbank.com/transfer?to=attacker&amount=1000">
```

**Protection:**
```python
# Use Flask-WTF for automatic CSRF protection
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
csrf = CSRFProtect(app)

# In templates, add CSRF token to forms:
<form method="POST">
    {{ csrf_token() }}
    <!-- rest of form -->
</form>
```

**Key Points:**
- Add CSRF tokens to all forms
- Verify tokens on submission
- Use `SameSite` cookies
- Check `Referer` header for sensitive operations

### Path Traversal

**Vulnerable Code:**
```python
# ❌ User can access any file
filename = request.args.get('file')
with open(f'uploads/{filename}', 'r') as f:
    return f.read()

# Attacker requests: ?file=../../etc/passwd
```

**Secure Code:**
```python
# ✅ Validate and sanitize paths
import os
from werkzeug.utils import secure_filename

filename = secure_filename(request.args.get('file', ''))
filepath = os.path.join('uploads', filename)

# Ensure file is within uploads directory
if not filepath.startswith(os.path.abspath('uploads')):
    return "Invalid file path", 400

with open(filepath, 'r') as f:
    return f.read()
```

---

## 4. Session Security

### Configure Sessions Properly

```python
from flask import Flask

app = Flask(__name__)

# Session configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Use environment variable!
app.config['SESSION_COOKIE_SECURE'] = True  # HTTPS only (disable in dev on localhost)
app.config['SESSION_COOKIE_HTTPONLY'] = True  # No JavaScript access
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # CSRF protection
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30 minutes

# For development on localhost (HTTP):
# app.config['SESSION_COOKIE_SECURE'] = False
```

### Generate Strong Secret Keys

```python
import secrets

# Generate a secure secret key
secret_key = secrets.token_hex(32)
print(secret_key)

# Store in .env file (never commit to git!)
# SECRET_KEY=a7f8d9e6c5b4a3f2e1d0c9b8a7f6e5d4c3b2a1f0e9d8c7b6a5f4e3d2c1b0a9f8
```

### Load from Environment

```python
import os
from dotenv import load_dotenv

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
if not app.config['SECRET_KEY']:
    raise ValueError("SECRET_KEY environment variable not set!")
```

---

## 5. File Upload Security

### Validate Uploads

```python
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file", 400
    
    file = request.files['file']
    
    # Validate filename
    if not file.filename or not allowed_file(file.filename):
        return "Invalid file type", 400
    
    # Sanitize filename
    filename = secure_filename(file.filename)
    
    # Check file size
    file.seek(0, os.SEEK_END)
    size = file.tell()
    if size > MAX_FILE_SIZE:
        return "File too large", 400
    file.seek(0)
    
    # Save file
    filepath = os.path.join('uploads', filename)
    file.save(filepath)
    
    return "File uploaded", 200
```

---

## 6. HTTPS and Transport Security

### Always Use HTTPS in Production

```python
# Force HTTPS in Flask
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app, force_https=True)
```

### Security Headers

```python
@app.after_request
def set_security_headers(response):
    # Prevent XSS
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    # Content Security Policy
    response.headers['Content-Security-Policy'] = \
        "default-src 'self'; script-src 'self'"
    
    return response
```

---

## 7. Rate Limiting

### Prevent Abuse

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")  # Only 5 login attempts per minute
def login():
    # Login logic
    pass
```

---

## 8. Security Checklist

### Before Deploying

- [ ] All passwords are hashed (never plain text)
- [ ] Using parameterized queries (no SQL injection)
- [ ] Templates auto-escape output (no XSS)
- [ ] CSRF protection enabled on forms
- [ ] Secret keys loaded from environment (not hardcoded)
- [ ] File uploads validated and sanitized
- [ ] HTTPS enabled (in production)
- [ ] Security headers set
- [ ] Rate limiting on sensitive endpoints
- [ ] User input validated and sanitized
- [ ] Error messages don't leak sensitive info
- [ ] Dependencies up to date (no known vulnerabilities)
- [ ] Database backups configured
- [ ] Logging enabled for security events

---

## 9. Testing Security

### Manual Testing

```bash
# Test SQL injection
curl -X POST http://localhost:5000/login \
     -d "username=' OR '1'='1&password=anything"

# Should fail! If it succeeds, you have SQL injection vulnerability

# Test XSS
curl -X POST http://localhost:5000/comment \
     -d "comment=<script>alert('xss')</script>"

# Check response - script should be escaped, not executed
```

### Automated Tools

```bash
# Install safety to check for vulnerable dependencies
pip install safety

# Check your dependencies
safety check

# Install bandit for Python security linting
pip install bandit

# Scan your code
bandit -r .
```

---

## 10. Resources

### Learn More
- **OWASP Top 10:** https://owasp.org/www-project-top-ten/
- **Flask Security:** https://flask.palletsprojects.com/en/latest/security/
- **Python Security:** https://python.readthedocs.io/en/stable/library/security.html

### Security Tools
- **safety** - Check dependencies for vulnerabilities
- **bandit** - Python security linter
- **sqlmap** - SQL injection testing
- **OWASP ZAP** - Web application security scanner

### Security Headers
- **securityheaders.com** - Test your headers
- **observatory.mozilla.org** - Security scanner

---

## Key Takeaways

1. **Never trust user input** - Always validate and sanitize
2. **Hash passwords** - Use bcrypt, pbkdf2, or Argon2
3. **Use parameterized queries** - Prevent SQL injection
4. **Auto-escape templates** - Prevent XSS
5. **Enable CSRF protection** - Protect forms
6. **Use HTTPS** - Encrypt all traffic
7. **Keep dependencies updated** - Patch vulnerabilities
8. **Follow least privilege** - Users should only access what they need

**Security is a journey, not a destination.** Keep learning and stay updated!

---

**Next:** [Debugging & Testing](../07-debugging-testing/)
