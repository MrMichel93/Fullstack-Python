# Practice Problems - Flask Setup & Installation

Before moving on, practice these exercises to solidify your Flask knowledge:

## Problem 1: Personal Portfolio Page
**Difficulty:** Easy  
**Time:** 15-20 minutes

Create a Flask application with the following features:
- A home page (`/`) that displays your name and a welcome message
- An about page (`/about`) that shows information about you
- A contact page (`/contact`) that displays your email
- Use template inheritance with a `base.html` template
- Add a navigation bar that works on all pages

**What you'll practice:**
- Creating multiple routes
- Using templates and template inheritance
- Using `url_for()` for navigation

---

## Problem 2: Dynamic Greeting App
**Difficulty:** Easy  
**Time:** 15-20 minutes

Create a Flask application that:
- Has a route `/greet/<name>` that displays a personalized greeting
- Has a route `/greet` (without name) that shows a default greeting
- Has a route `/greet?name=<name>&time=<morning|afternoon|evening>` that shows time-specific greetings
- Displays different greetings based on the time parameter (e.g., "Good morning, Alice!")
- Add a CSS file in the `static/` folder to style your greetings

**What you'll practice:**
- Routes with parameters
- URL query parameters with `request.args`
- Serving static files (CSS)
- Conditional logic in templates

---

## Problem 3: Simple Form Handler
**Difficulty:** Medium  
**Time:** 20-30 minutes

Create a Flask application with a feedback form:
- A page with a form that accepts: name, email, and message
- Form should submit to `/submit` using POST method
- After submission, redirect to a thank you page (`/thank-you`)
- Display a flash message on the thank you page: "Thank you [name], we received your message!"
- If any field is empty, show an error flash message and redisplay the form
- Style the form with CSS

**What you'll practice:**
- HTML forms with POST method
- Getting form data with `request.form`
- Redirects with `redirect()` and `url_for()`
- Flash messages for user feedback
- Basic form validation

**Bonus Challenge:**
- Save submitted feedback to a list (stored in memory)
- Create a `/feedback` route that displays all submitted feedback

---

## 📝 Practice Problems Now Available as Code!

**NEW:** These practice problems are now available as individual Python files with automated tests!

### How to Use

1. Navigate to the `problems/` directory:
   ```bash
   cd modules/00-flask-setup/problems/
   ```

2. Read the problem description in each Python file
3. Complete the TODO sections
4. Run tests to verify your solution:
   ```bash
   pytest test_problem1.py -v  # For Problem 1
   pytest test_problem2.py -v  # For Problem 2
   pytest test_problem3.py -v  # For Problem 3
   ```

### Available Files

- **Problem 1:** `problem1_portfolio.py` + `test_problem1.py`
- **Problem 2:** `problem2_greeting.py` + `test_problem2.py`
- **Problem 3:** `problem3_form.py` + `test_problem3.py`

See `problems/README.md` for detailed instructions!

---

## Next Steps

After completing these practice problems:

1. ✅ You can create routes and templates
2. ✅ You understand form handling
3. ✅ You know how to use static files
4. ✅ You're familiar with Flask patterns

**Continue to:** [Architecture Primer](../01-architecture-primer/) to understand web fundamentals before building projects.
