# Project 2: URL Shortener

## 🔗 What You'll Build
A URL shortening service (like bit.ly or tinyurl.com) where users can:
- Submit long URLs
- Get short codes
- Use short codes to redirect to original URLs
- View click statistics

## 🎯 Learning Objectives

### Backend Concepts
- **URL generation** - Creating unique short codes
- **HTTP redirects** - 301/302 status codes
- **Database queries** - Finding records by unique keys
- **Click tracking** - Incrementing counters

### Frontend Concepts
- **Form validation** - Checking URL format
- **Result display** - Showing generated links
- **Copy to clipboard** - JavaScript interaction
- **Click statistics** - Data visualization

## 🛠️ Tech Stack
- **Backend:** Flask or FastAPI
- **Database:** SQLite
- **Frontend:** HTML + CSS + minimal JS

## 📂 Project Structure

```
03-url-shortener/
├── README.md
├── challenges.md
├── starter/
│   └── flask_version/
│       ├── app.py (TODO: Complete the TODOs)
│       ├── templates/
│       │   ├── base.html
│       │   ├── index.html (TODO: Complete the TODOs)
│       │   └── stats.html
│       └── static/
│           └── style.css
└── solution/
    └── flask_version/ (complete working code)
```

## 🚀 Getting Started

### 1. Install Dependencies

```bash
cd 03-url-shortener/starter/flask_version
pip install -r requirements.txt
```

### 2. Run the App

```bash
python app.py
```

Visit `http://localhost:5000`

## ✅ TODO Checklist

### Part 1: Database Setup (20 min)
- [ ] Complete `init_db()` to create the `urls` table
- [ ] Table needs: id, original_url, short_code, clicks, created_at
- [ ] Test: Run app, check that database is created

### Part 2: Generate Short Codes (30 min)
- [ ] Complete `generate_short_code()` function
- [ ] Use random string generation (letters + numbers)
- [ ] Check for uniqueness in database
- [ ] Test: Generate multiple codes, verify they're different

### Part 3: Create Short URLs (30 min)
- [ ] Complete `shorten()` route to handle form submissions
- [ ] Validate URL format
- [ ] Generate short code
- [ ] Save to database
- [ ] Test: Submit URLs and verify they're saved

### Part 4: Redirect Handler (20 min)
- [ ] Complete `redirect_to_url()` route
- [ ] Look up short code in database
- [ ] Increment click counter
- [ ] Return 301 redirect or 404
- [ ] Test: Visit shortened URLs

### Part 5: Statistics Page (30 min)
- [ ] Complete `stats()` route to show all URLs
- [ ] Display original URL, short code, and clicks
- [ ] Add sorting by clicks or date
- [ ] Test: View stats page

### Part 6: Frontend (30 min)
- [ ] Complete form in `index.html`
- [ ] Display shortened URL result
- [ ] Add "Copy to clipboard" button (JavaScript)
- [ ] Style the page
- [ ] Test: Complete user flow

**Total Time: ~2.5 hours**

## 🧪 Testing Your App

1. **URL Shortening:**
   - Submit: `https://www.example.com/very/long/url`
   - Should get: `http://localhost:5000/abc123`
   - Copy and paste should work

2. **Redirect:**
   - Visit: `http://localhost:5000/abc123`
   - Should redirect to original URL
   - Click count should increment

3. **Statistics:**
   - View `/stats` page
   - Should see all shortened URLs
   - Click counts should be accurate

4. **Edge Cases:**
   - Invalid URL format
   - Duplicate URLs (should create new short code or reuse?)
   - Very long URLs (1000+ characters)
   - Short code collision (very rare)

## 📊 Database Schema

```sql
CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT NOT NULL,
    short_code TEXT UNIQUE NOT NULL,
    clicks INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🎨 Features Checklist

- [ ] Shorten long URLs
- [ ] Generate unique short codes (6 characters)
- [ ] Redirect short URLs to original URLs
- [ ] Track click counts
- [ ] Display statistics for all URLs
- [ ] Copy shortened URL to clipboard
- [ ] URL validation

## 🐛 Common Issues & Solutions

### Invalid URL format
```python
# Basic validation
if not original_url.startswith(('http://', 'https://')):
    original_url = 'https://' + original_url
```

### Short code collisions
```python
# Keep generating until unique
while True:
    code = generate_short_code()
    existing = db.execute("SELECT id FROM urls WHERE short_code=?", (code,)).fetchone()
    if not existing:
        break
```

### Copy to clipboard not working
```javascript
// Use modern Clipboard API
navigator.clipboard.writeText(url).then(() => {
    alert('Copied!');
});
```

## 💡 Key Concepts

### HTTP Redirects
```python
# 301 - Permanent Redirect (cached by browser)
return redirect(url, code=301)

# 302 - Temporary Redirect (not cached)
return redirect(url, code=302)
```

### URL Validation
```python
import re

def is_valid_url(url):
    pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return pattern.match(url) is not None
```

### Generating Random Codes
```python
import random
import string

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choice(chars) for _ in range(length))
```

## 🎓 What You Learned

After completing this project, you understand:

1. **URL Routing:** Dynamic routes with parameters (/<code>)
2. **Redirects:** How to send users to different URLs
3. **Random Generation:** Creating unique identifiers
4. **Click Tracking:** Incrementing database values
5. **JavaScript Basics:** Clipboard API and DOM manipulation

## 📚 Next Steps

1. ✅ Complete all TODOs
2. ✅ Test all features thoroughly
3. ✅ Try [Extension Challenges](./challenges.md)
4. ✅ Move to **[Simple Blog](../04-simple-blog/)** project

## 🏆 Extension Ideas

See [challenges.md](./challenges.md) for ideas like:
- Custom short codes (user-chosen)
- QR code generation
- Link expiration dates
- Analytics dashboard
- API for programmatic access

---

**Ready?** Open `starter/flask_version/app.py` and start coding!
