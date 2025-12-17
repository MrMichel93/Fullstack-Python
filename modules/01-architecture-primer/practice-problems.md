# Practice Problems - Architecture Primer

Test your understanding of web architecture with these exercises:

## Problem 1: Trace the Request Journey
**Difficulty:** Easy  
**Time:** 10-15 minutes

**Scenario:** A user visits `http://myapp.com/profile/john` to view John's profile.

Write out step-by-step what happens:
1. What does the browser do?
2. What HTTP method is used?
3. What does the server receive?
4. How does the server find the right route?
5. What does the server do (assume it queries a database)?
6. What does the server send back?
7. What does the browser do with the response?

**Extension:** Now trace what happens when the user clicks "Edit Profile" button and submits a form with updated information.

**What you'll practice:**
- Understanding the request/response lifecycle
- HTTP methods (GET vs POST)
- Client-server communication

---

## Problem 2: Design a URL Structure
**Difficulty:** Easy  
**Time:** 10-15 minutes

You're building a blog application. Design appropriate URLs and HTTP methods for these operations:

1. Show list of all blog posts
2. Show a single blog post
3. Create a new blog post
4. Edit an existing blog post
5. Delete a blog post
6. Show posts by a specific author
7. Show posts from a specific category

For each operation, specify:
- The URL pattern (e.g., `/posts`, `/posts/<id>`)
- The HTTP method (GET, POST, PUT, DELETE)
- What data flows from client to server (if any)
- What data flows from server to client

**What you'll practice:**
- RESTful URL design
- Choosing appropriate HTTP methods
- Understanding data flow

---

## Problem 3: Debug the Architecture
**Difficulty:** Medium  
**Time:** 15-20 minutes

**Scenario:** A student built their first Flask app but things aren't working. Help them debug!

**Problem 1:** "When I submit my form, nothing happens!"
```python
@app.route('/contact')
def contact():
    name = request.form['name']
    return f"Thanks, {name}!"
```
- What's wrong?
- How would you fix it?

**Problem 2:** "I get a KeyError when accessing the page!"
```python
@app.route('/profile')
def profile():
    username = request.args['username']
    return f"Profile for {username}"
```
- What happens when user visits `/profile` without parameters?
- How would you fix it?

**Problem 3:** "My page shows `<h1>Hello</h1>` as text instead of a heading!"
```python
@app.route('/')
def home():
    content = "<h1>Hello</h1>"
    return render_template('home.html', content=content)
```
```html
<!-- home.html -->
<div>{{ content }}</div>
```
- What's causing this?
- How would you fix it?

**What you'll practice:**
- Understanding HTTP methods in routes
- Safe parameter handling
- Template auto-escaping behavior

---

## Quick Reference

### HTTP Status Codes
- `200 OK` - Success
- `201 Created` - Resource created
- `400 Bad Request` - Invalid client request
- `404 Not Found` - Resource doesn't exist
- `500 Internal Server Error` - Server error

### Common Headers
- `Content-Type: text/html` - Response contains HTML
- `Content-Type: application/json` - Response contains JSON
- `Location: /notes` - Redirect to this URL

### URL Parts
```
http://localhost:5000/notes/5?sort=date#top
│      │         │    │      │       │
scheme   host    port  path  query  fragment
```

---

## 📝 Practice Problems Now Available as Code!

**NEW:** These practice problems are now available as individual Python files with automated tests!

### How to Use

1. Navigate to the `problems/` directory:
   ```bash
   cd modules/01-architecture-primer/problems/
   ```

2. Read the problem description in each Python file
3. Complete the TODO sections (fill in functions with your understanding)
4. Run tests to verify your solution:
   ```bash
   pytest test_problem1.py -v  # For Problem 1
   pytest test_problem2.py -v  # For Problem 2
   pytest test_problem3.py -v  # For Problem 3
   ```

### Available Files

- **Problem 1:** `problem1_request_journey.py` + `test_problem1.py`
- **Problem 2:** `problem2_url_design.py` + `test_problem2.py`
- **Problem 3:** `problem3_debug_code.py` + `test_problem3.py`

See `problems/README.md` for detailed instructions!

---

## Ready for Projects?

Now that you understand:
- ✅ Client vs Server roles
- ✅ Request/Response cycle
- ✅ Data flow through an app
- ✅ Key web components

You're ready to build your first project!

**Next:** [Notes App](../../projects/02-notes-app/) - Build a CRUD application
