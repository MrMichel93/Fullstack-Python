# Practice Problems - Security Basics

Apply security concepts with these hands-on exercises:

## Problem 1: Secure User Registration
**Difficulty:** Medium  
**Time:** 25-30 minutes

Create a Flask application with a secure user registration system:

**Requirements:**
1. Registration form with: username, email, password, confirm password
2. Password validation:
   - At least 8 characters
   - Contains at least one uppercase letter
   - Contains at least one number
   - Contains at least one special character
3. Hash passwords using `werkzeug.security.generate_password_hash()`
4. Store users in SQLite database (table: users with id, username, email, password_hash)
5. Check if username/email already exists before registration
6. Show appropriate error messages for validation failures
7. After successful registration, show success message

**What you'll practice:**
- Password hashing (never storing plain text)
- Input validation
- Database interaction with parameterized queries
- User feedback with flash messages

**Test your work:**
- Try registering with weak passwords (should fail)
- Try registering with same username twice (should fail)
- Register successfully and verify password is hashed in database

---

## Problem 2: Prevent Security Vulnerabilities
**Difficulty:** Medium  
**Time:** 20-25 minutes

You've been given a Flask app with security vulnerabilities. Fix all the issues!

**Vulnerable Code (intentionally insecure for learning purposes):**
```python
@app.route('/search')
def search():
    query = request.args.get('q', '')
    # Show search query back to user
    return f"<h1>Search results for: {query}</h1>"

@app.route('/user/<username>')
def user_profile(username):
    # Get user from database
    db = get_db()
    sql = f"SELECT * FROM users WHERE username = '{username}'"
    user = db.execute(sql).fetchone()
    return render_template('profile.html', user=user)

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    # Anyone can delete any note by visiting the URL
    db = get_db()
    db.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    db.commit()
    return redirect('/')
```

**Your tasks:**
1. Fix the XSS vulnerability in the search route
2. Fix the SQL injection vulnerability in the user profile route
3. Add CSRF protection to the delete operation (change to POST with token)
4. Add authentication check (only owner can delete their notes)

**What you'll practice:**
- Preventing XSS attacks
- Preventing SQL injection
- CSRF protection
- Authorization and access control

---

## Problem 3: Secure File Upload
**Difficulty:** Medium  
**Time:** 25-30 minutes

Create a secure file upload feature for a Flask application:

**Requirements:**
1. Upload form that accepts image files only
2. Validate file extensions (only allow: jpg, jpeg, png, gif)
3. Validate file size (max 5MB)
4. Use `secure_filename()` to sanitize filenames
5. Save files to an `uploads/` directory
6. Generate unique filenames to prevent overwriting
7. Display uploaded image on a success page
8. Handle errors gracefully (file too large, wrong type, etc.)

**Security checklist:**
- ✅ File extension validation
- ✅ File size limitation
- ✅ Filename sanitization
- ✅ Unique filenames
- ✅ Appropriate error messages
- ✅ Store uploads outside web root (if possible)

**What you'll practice:**
- Secure file upload handling
- Input validation
- Error handling
- Using `werkzeug.utils.secure_filename()`

**Bonus Challenge:**
- Add virus scanning (research `pyclamd` library)
- Validate file content, not just extension (check magic bytes)
- Implement file size check before upload (client-side and server-side)

---

## Resources

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
