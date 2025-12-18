# Practice Problems - URL Shortener

Before moving on, practice these exercises to master redirects and ID generation:

## Problem 1: Basic URL Shortener
**Difficulty:** Medium  
**Time:** 30-40 minutes

Create a Flask application that shortens URLs:
- Home page with a form to submit long URLs
- Generate a 6-character random short code
- Store short code and long URL in SQLite database
- Display the shortened URL after submission
- Redirect users when they visit the short URL (`/<short_code>`)
- Show "404 Not Found" for invalid short codes

**What you'll practice:**
- Random string generation
- Database INSERT and SELECT
- HTTP redirects (302)
- Dynamic routing with parameters

---

## Problem 2: URL Shortener with Click Tracking
**Difficulty:** Medium  
**Time:** 30-40 minutes

Extend the basic URL shortener to track clicks:
- Add a `clicks` column to the database (default 0)
- Increment the click counter each time someone uses the short URL
- Create a statistics page (`/stats/<short_code>`) showing:
  - Original URL
  - Short URL
  - Total clicks
  - Creation date
- Display a list of all shortened URLs with their click counts

**What you'll practice:**
- UPDATE queries with incrementing
- Statistics display
- Data tables
- Multiple related pages

---

## Problem 3: URL Shortener with Copy Feature
**Difficulty:** Medium  
**Time:** 30-40 minutes

Add frontend features to your URL shortener:
- Add a "Copy to Clipboard" button next to the shortened URL
- Use JavaScript to implement the copy functionality
- Show a "Copied!" message after successful copy
- Add URL validation to reject invalid URLs
- Style the application with CSS for better UX
- Add a QR code generator for shortened URLs (bonus)

**What you'll practice:**
- JavaScript clipboard API
- URL validation
- User feedback mechanisms
- Frontend/backend integration

**Bonus Challenge:**
- Custom short codes (let users choose their own code)
- Expiration dates (URLs expire after X days)
- Password protection for URLs
- Analytics (track clicks by date, referrer, etc.)

---

## 📝 Practice Problems Now Available as Code!

**NEW:** These practice problems are now available as individual Python files with automated tests!

### How to Use

1. Navigate to the `problems/` directory:
   ```bash
   cd modules/03-url-shortener/problems/
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

- **Problem 1:** `problem1_basic_shortener.py` + `test_problem1.py`
- **Problem 2:** `problem2_click_tracking.py` + `test_problem2.py`
- **Problem 3:** `problem3_copy_feature.py` + `test_problem3.py`

See `problems/README.md` for detailed instructions!

---

## Next Steps

After completing these practice problems:

1. ✅ You can generate unique IDs
2. ✅ You understand HTTP redirects
3. ✅ You can track user actions
4. ✅ You know how to validate input

**Continue to:** [Simple Blog](../04-simple-blog/) to learn about multi-page applications.
