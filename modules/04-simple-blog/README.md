# Simple Blog - Multi-Page Applications & Navigation

## What You'll Learn
- Multi-page routing
- Query parameters and filtering
- Template inheritance
- Static file serving
- Navigation menus
- CSS layouts (Flexbox/Grid)
- Responsive design
- Typography and readability

---

## 1. Multi-Page Application Structure

### What is a Multi-Page Application?

A **multi-page application (MPA)** has multiple distinct pages, each with its own URL:
- Home page: `/`
- About page: `/about`
- Blog posts: `/posts`
- Individual post: `/posts/123`
- Contact: `/contact`

Each page can have different layouts, content, and functionality.

### Organizing Routes

```python
# Organize routes by functionality
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts')
def posts_list():
    posts = get_all_posts()
    return render_template('posts.html', posts=posts)

@app.route('/posts/<int:post_id>')
def view_post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/contact')
def contact():
    return render_template('contact.html')
```

---

## 2. Template Inheritance

### Base Template Pattern

Create a base template that other templates extend:

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Blog{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav>
        <div class="container">
            <a href="/" class="logo">My Blog</a>
            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/posts">Posts</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </div>
    </nav>
    
    <main class="container">
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <div class="container">
            <p>&copy; 2024 My Blog. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

### Child Templates

```html
<!-- templates/home.html -->
{% extends "base.html" %}

{% block title %}Home - My Blog{% endblock %}

{% block content %}
    <h1>Welcome to My Blog</h1>
    <p>Latest posts and updates</p>
    
    <div class="posts-grid">
        {% for post in recent_posts %}
            <article class="post-card">
                <h2>{{ post.title }}</h2>
                <p>{{ post.excerpt }}</p>
                <a href="/posts/{{ post.id }}">Read more</a>
            </article>
        {% endfor %}
    </div>
{% endblock %}
```

---

## 3. Navigation Patterns

### Active Navigation Highlighting

```python
# Pass current page to template
@app.route('/')
def home():
    return render_template('home.html', current_page='home')

@app.route('/posts')
def posts():
    return render_template('posts.html', current_page='posts')
```

```html
<!-- In base.html -->
<nav>
    <a href="/" {% if current_page == 'home' %}class="active"{% endif %}>Home</a>
    <a href="/posts" {% if current_page == 'posts' %}class="active"{% endif %}>Posts</a>
    <a href="/about" {% if current_page == 'about' %}class="active"{% endif %}>About</a>
</nav>
```

### Breadcrumb Navigation

```html
<nav class="breadcrumb">
    <a href="/">Home</a>
    <span>/</span>
    <a href="/posts">Posts</a>
    <span>/</span>
    <span class="current">{{ post.title }}</span>
</nav>
```

---

## 4. Query Parameters and Filtering

### Filtering Posts by Category

```python
@app.route('/posts')
def posts_list():
    category = request.args.get('category')
    
    db = get_db()
    
    if category:
        posts = db.execute(
            'SELECT * FROM posts WHERE category = ? ORDER BY created_at DESC',
            (category,)
        ).fetchall()
    else:
        posts = db.execute(
            'SELECT * FROM posts ORDER BY created_at DESC'
        ).fetchall()
    
    db.close()
    
    return render_template('posts.html', posts=posts, current_category=category)
```

```html
<!-- Category filter links -->
<div class="category-filter">
    <a href="/posts" {% if not current_category %}class="active"{% endif %}>All</a>
    <a href="/posts?category=Technology" 
       {% if current_category == 'Technology' %}class="active"{% endif %}>
        Technology
    </a>
    <a href="/posts?category=Travel" 
       {% if current_category == 'Travel' %}class="active"{% endif %}>
        Travel
    </a>
</div>
```

### Search Functionality

```python
@app.route('/posts/search')
def search_posts():
    query = request.args.get('q', '')
    
    db = get_db()
    posts = db.execute(
        'SELECT * FROM posts WHERE title LIKE ? OR content LIKE ?',
        (f'%{query}%', f'%{query}%')
    ).fetchall()
    db.close()
    
    return render_template('search.html', posts=posts, query=query)
```

---

## 5. CSS Layouts

### Flexbox for Navigation

```css
nav {
    background-color: #333;
    padding: 1rem 0;
}

.nav-links {
    display: flex;
    list-style: none;
    gap: 2rem;
    align-items: center;
}

.nav-links a {
    color: white;
    text-decoration: none;
}

.nav-links a:hover {
    color: #4CAF50;
}
```

### Grid for Post Layouts

```css
.posts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.post-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 1.5rem;
    transition: box-shadow 0.3s;
}

.post-card:hover {
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
```

---

## 6. Responsive Design

### Mobile-First Approach

```css
/* Mobile styles (default) */
.container {
    width: 100%;
    padding: 0 1rem;
}

.posts-grid {
    grid-template-columns: 1fr;
}

/* Tablet */
@media (min-width: 768px) {
    .container {
        max-width: 720px;
        margin: 0 auto;
    }
    
    .posts-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Desktop */
@media (min-width: 1024px) {
    .container {
        max-width: 960px;
    }
    
    .posts-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

### Responsive Navigation

```css
/* Mobile menu */
@media (max-width: 767px) {
    .nav-links {
        flex-direction: column;
        display: none;
    }
    
    .nav-links.active {
        display: flex;
    }
    
    .menu-toggle {
        display: block;
    }
}
```

---

## 7. Typography and Readability

### Font Choices

```css
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
    line-height: 1.6;
    color: #333;
}

h1, h2, h3 {
    font-weight: 600;
    line-height: 1.2;
    margin-bottom: 1rem;
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.5rem; }

.post-content {
    font-size: 1.125rem;
    line-height: 1.8;
    max-width: 700px;
}
```

### Reading Experience

```css
.post-content p {
    margin-bottom: 1.5rem;
}

.post-content img {
    max-width: 100%;
    height: auto;
    border-radius: 8px;
    margin: 2rem 0;
}

.post-content blockquote {
    border-left: 4px solid #4CAF50;
    padding-left: 1.5rem;
    margin: 2rem 0;
    font-style: italic;
    color: #666;
}
```

---

## 8. Static File Organization

### Directory Structure

```
static/
├── css/
│   ├── style.css
│   └── responsive.css
├── js/
│   └── main.js
└── images/
    ├── logo.png
    └── posts/
        └── post-1.jpg
```

### Serving Static Files

```html
<!-- CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

<!-- JavaScript -->
<script src="{{ url_for('static', filename='js/main.js') }}"></script>

<!-- Images -->
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
```

---

## 9. Practice Problems

Ready to build a blog? Complete the **[Practice Problems](./practice-problems.md)** to master multi-page applications!

**What you'll build:**
- Multi-page blog with navigation
- Post listing and detail pages
- Category filtering
- Responsive design
- Professional styling

These exercises will help you create complete web applications with multiple pages.

---

## 10. Quick Reference

### Template Inheritance
```html
<!-- base.html -->
{% block content %}{% endblock %}

<!-- child.html -->
{% extends "base.html" %}
{% block content %}...{% endblock %}
```

### Query Parameters
```python
category = request.args.get('category')
posts = db.execute('SELECT * FROM posts WHERE category = ?', (category,))
```

### Responsive CSS
```css
@media (min-width: 768px) {
    .grid { grid-template-columns: repeat(2, 1fr); }
}
```

---

## 11. Next Steps

After completing this module:

1. ✅ You can build multi-page applications
2. ✅ You understand template inheritance
3. ✅ You can create responsive layouts
4. ✅ You know how to organize navigation

**Continue to:** [Inventory Tracker](../05-inventory-tracker/) to learn about user authentication.

---

**Ready to build a blog?** Head to [Practice Problems](./practice-problems.md)!
