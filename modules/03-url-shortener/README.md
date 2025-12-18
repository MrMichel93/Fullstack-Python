# URL Shortener - Redirects & ID Generation

## What You'll Learn
- Random string generation
- HTTP redirects (301 vs 302)
- Dynamic routing with parameters
- Click tracking and counters
- JavaScript clipboard API
- Result display patterns
- Data tables
- URL validation

---

## 1. URL Shortening Overview

### What is a URL Shortener?

A URL shortener takes long URLs and creates short, memorable links:
- **Long URL:** `https://example.com/blog/posts/2024/01/my-very-long-article-title`
- **Short URL:** `http://short.link/abc123`

**Benefits:**
- Easier to share (especially on social media with character limits)
- Cleaner appearance in print materials
- Track click statistics
- Update destination without changing short link

---

## 2. Generating Short Codes

### Random String Generation

```python
import string
import random

def generate_short_code(length=6):
    """Generate a random short code for URL."""
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    short_code = ''.join(random.choice(characters) for _ in range(length))
    return short_code

# Examples: "aB3xYz", "9mK2pQ", "Hn7LqR"
```

### Checking for Uniqueness

```python
def generate_unique_code():
    """Generate a unique short code that doesn't exist in database."""
    db = get_db()
    
    while True:
        code = generate_short_code()
        
        # Check if code already exists
        existing = db.execute(
            'SELECT id FROM urls WHERE short_code = ?',
            (code,)
        ).fetchone()
        
        if existing is None:
            # Code is unique!
            db.close()
            return code
```

### Alternative: Sequential IDs

```python
def encode_id(num):
    """Convert database ID to base62 string."""
    alphabet = string.ascii_letters + string.digits
    base = len(alphabet)
    
    encoded = ''
    while num > 0:
        encoded = alphabet[num % base] + encoded
        num //= base
    
    return encoded or alphabet[0]

# Example: ID 12345 -> "3d7"
```

---

## 3. HTTP Redirects

### Understanding Redirect Status Codes

**302 Found (Temporary Redirect):**
```python
from flask import redirect

@app.route('/<short_code>')
def redirect_to_url(short_code):
    # 302 redirect (default)
    return redirect(long_url)
```

**301 Moved Permanently:**
```python
@app.route('/<short_code>')
def redirect_to_url(short_code):
    # 301 redirect
    return redirect(long_url, code=301)
```

**When to use each:**
- **302** - URL might change, want to track clicks
- **301** - URL is permanent, better for SEO

**For URL shorteners, use 302** because:
- Allows updating the destination URL
- Ensures clicks go through your server (for tracking)
- More flexible

---

## 4. Database Schema for URL Shortener

### Basic Schema

```python
def init_db():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE NOT NULL,
            long_url TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            clicks INTEGER DEFAULT 0
        )
    ''')
    db.commit()
    db.close()
```

### Creating Short URLs

```python
@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['url']
    
    # Generate unique short code
    short_code = generate_unique_code()
    
    # Save to database
    db = get_db()
    db.execute(
        'INSERT INTO urls (short_code, long_url) VALUES (?, ?)',
        (short_code, long_url)
    )
    db.commit()
    db.close()
    
    # Return short URL
    short_url = request.host_url + short_code
    return render_template('result.html', short_url=short_url)
```

---

## 5. Handling Redirects

### Basic Redirect Implementation

```python
@app.route('/<short_code>')
def redirect_to_url(short_code):
    db = get_db()
    
    # Find the URL
    url_data = db.execute(
        'SELECT long_url FROM urls WHERE short_code = ?',
        (short_code,)
    ).fetchone()
    
    db.close()
    
    if url_data is None:
        return "Short URL not found", 404
    
    long_url = url_data['long_url']
    return redirect(long_url)
```

### With Click Tracking

```python
@app.route('/<short_code>')
def redirect_to_url(short_code):
    db = get_db()
    
    # Find the URL
    url_data = db.execute(
        'SELECT long_url FROM urls WHERE short_code = ?',
        (short_code,)
    ).fetchone()
    
    if url_data is None:
        db.close()
        return "Short URL not found", 404
    
    # Increment click counter
    db.execute(
        'UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?',
        (short_code,)
    )
    db.commit()
    db.close()
    
    long_url = url_data['long_url']
    return redirect(long_url)
```

---

## 6. URL Validation

### Basic URL Validation

```python
from urllib.parse import urlparse

def is_valid_url(url):
    """Check if URL is valid."""
    try:
        result = urlparse(url)
        # Must have scheme (http/https) and network location (domain)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

# Usage
@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.form['url']
    
    if not is_valid_url(long_url):
        flash('Please enter a valid URL', 'error')
        return redirect(url_for('index'))
    
    # ... proceed with shortening
```

### Adding HTTP Prefix

```python
def normalize_url(url):
    """Ensure URL has http:// or https:// prefix."""
    url = url.strip()
    
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    return url

# Usage
long_url = normalize_url(request.form['url'])
```

---

## 7. Statistics and Analytics

### Tracking Clicks

```python
@app.route('/stats/<short_code>')
def show_stats(short_code):
    db = get_db()
    
    url_data = db.execute(
        'SELECT * FROM urls WHERE short_code = ?',
        (short_code,)
    ).fetchone()
    
    db.close()
    
    if url_data is None:
        return "Short URL not found", 404
    
    return render_template('stats.html', url=url_data)
```

### Statistics Template

```html
<!-- stats.html -->
<h1>Statistics for {{ url.short_code }}</h1>

<div class="stats-grid">
    <div class="stat-card">
        <h3>Short URL</h3>
        <p>{{ request.host_url }}{{ url.short_code }}</p>
    </div>
    
    <div class="stat-card">
        <h3>Original URL</h3>
        <p>{{ url.long_url }}</p>
    </div>
    
    <div class="stat-card">
        <h3>Total Clicks</h3>
        <p class="big-number">{{ url.clicks }}</p>
    </div>
    
    <div class="stat-card">
        <h3>Created</h3>
        <p>{{ url.created_at }}</p>
    </div>
</div>
```

---

## 8. Frontend Features

### Copy to Clipboard with JavaScript

```html
<div class="result">
    <input type="text" id="short-url" value="{{ short_url }}" readonly>
    <button onclick="copyToClipboard()">Copy</button>
    <span id="copy-status"></span>
</div>

<script>
function copyToClipboard() {
    const input = document.getElementById('short-url');
    input.select();
    document.execCommand('copy');
    
    const status = document.getElementById('copy-status');
    status.textContent = 'Copied!';
    setTimeout(() => status.textContent = '', 2000);
}
</script>
```

### Modern Clipboard API

```html
<script>
async function copyToClipboard() {
    const input = document.getElementById('short-url');
    
    try {
        await navigator.clipboard.writeText(input.value);
        showMessage('Copied!');
    } catch (err) {
        // Fallback for older browsers
        input.select();
        document.execCommand('copy');
        showMessage('Copied!');
    }
}

function showMessage(text) {
    const status = document.getElementById('copy-status');
    status.textContent = text;
    setTimeout(() => status.textContent = '', 2000);
}
</script>
```

---

## 9. Displaying URL List

### Show All Shortened URLs

```python
@app.route('/urls')
def list_urls():
    db = get_db()
    urls = db.execute(
        'SELECT * FROM urls ORDER BY created_at DESC'
    ).fetchall()
    db.close()
    
    return render_template('list.html', urls=urls)
```

### Data Table Template

```html
<!-- list.html -->
<h1>All Shortened URLs</h1>

<table>
    <thead>
        <tr>
            <th>Short Code</th>
            <th>Original URL</th>
            <th>Clicks</th>
            <th>Created</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for url in urls %}
        <tr>
            <td>
                <a href="/{{ url.short_code }}" target="_blank">
                    {{ url.short_code }}
                </a>
            </td>
            <td class="long-url">{{ url.long_url }}</td>
            <td>{{ url.clicks }}</td>
            <td>{{ url.created_at }}</td>
            <td>
                <a href="/stats/{{ url.short_code }}">Stats</a>
                <button onclick="copyLink('{{ request.host_url }}{{ url.short_code }}')">
                    Copy
                </button>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

---

## 10. Security Considerations

### Prevent URL Injection

```python
from urllib.parse import urlparse

BLOCKED_SCHEMES = ['javascript', 'data', 'file']

def is_safe_url(url):
    """Check if URL is safe to redirect to."""
    parsed = urlparse(url)
    
    # Block dangerous schemes
    if parsed.scheme.lower() in BLOCKED_SCHEMES:
        return False
    
    return True
```

### Rate Limiting

```python
from collections import defaultdict
import time

# Simple in-memory rate limiter
request_counts = defaultdict(list)

def is_rate_limited(ip, max_requests=10, window=60):
    """Check if IP has exceeded rate limit."""
    now = time.time()
    
    # Remove old requests outside the window
    request_counts[ip] = [
        timestamp for timestamp in request_counts[ip]
        if now - timestamp < window
    ]
    
    # Check if over limit
    if len(request_counts[ip]) >= max_requests:
        return True
    
    # Record this request
    request_counts[ip].append(now)
    return False

# Usage
@app.route('/shorten', methods=['POST'])
def shorten_url():
    ip = request.remote_addr
    
    if is_rate_limited(ip):
        return "Rate limit exceeded. Try again later.", 429
    
    # ... proceed with shortening
```

---

## 11. Practice Problems

Ready to build a URL shortener? Complete the **[Practice Problems](./practice-problems.md)** to apply what you've learned!

**What you'll build:**
- Basic URL shortening service
- Click tracking system
- Statistics dashboard
- Copy to clipboard feature

These exercises will help you master redirects and unique ID generation.

---

## 12. Quick Reference

### Generate Short Code
```python
import random
import string

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
```

### Create Short URL
```python
@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['url']
    code = generate_unique_code()
    db.execute('INSERT INTO urls (short_code, long_url) VALUES (?, ?)', 
               (code, long_url))
    db.commit()
    return render_template('result.html', short_url=f"{request.host_url}{code}")
```

### Redirect with Click Tracking
```python
@app.route('/<short_code>')
def redirect_url(short_code):
    db.execute('UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?', 
               (short_code,))
    db.commit()
    url = db.execute('SELECT long_url FROM urls WHERE short_code = ?', 
                     (short_code,)).fetchone()
    return redirect(url['long_url'])
```

---

## 13. Next Steps

After completing this module:

1. ✅ You understand HTTP redirects
2. ✅ You can generate unique IDs
3. ✅ You can track analytics
4. ✅ You know how to validate URLs

**Continue to:** [Simple Blog](../04-simple-blog/) to learn about multi-page applications and navigation.

---

**Ready to shorten some URLs?** Head to [Practice Problems](./practice-problems.md)!
