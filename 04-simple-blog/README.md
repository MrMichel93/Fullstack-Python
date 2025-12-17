# Project 3: Simple Blog

## 📰 What You'll Build
A multi-page blog application where users can:
- Read blog posts
- Create new posts
- View posts by category
- Navigate between pages
- See formatted content

## 🎯 Learning Objectives

### Backend Concepts
- **Multi-page routing** - Multiple connected pages
- **Template inheritance** - Reusing layouts with `{% extends %}`
- **Static files** - Serving CSS, images, JavaScript
- **URL parameters** - Query strings and path parameters

### Frontend Concepts
- **Navigation menus** - Links between pages
- **CSS layouts** - Flexbox and Grid
- **Responsive design** - Mobile-friendly layouts
- **Typography** - Making content readable

## 🛠️ Tech Stack
- **Backend:** Flask or FastAPI
- **Database:** SQLite
- **Frontend:** HTML + CSS (advanced styling)

## 📂 Project Structure

```
04-simple-blog/
├── README.md
├── challenges.md
├── starter/
│   └── flask_version/
│       ├── app.py
│       ├── templates/
│       │   ├── base.html
│       │   ├── home.html
│       │   ├── post.html
│       │   ├── create.html
│       │   └── category.html
│       └── static/
│           ├── css/
│           │   └── style.css
│           └── images/
└── solution/
    └── flask_version/
```

## ✅ TODO Checklist

### Part 1: Database & Models (30 min)
- [ ] Create posts table (id, title, content, category, author, created_at)
- [ ] Create categories table
- [ ] Add sample posts for testing

### Part 2: Homepage (30 min)
- [ ] List all posts (title, excerpt, date)
- [ ] Show latest posts first
- [ ] Add category filters

### Part 3: Single Post View (30 min)
- [ ] Create post detail page
- [ ] Display full content
- [ ] Show metadata (author, date, category)

### Part 4: Create Post (30 min)
- [ ] Build post creation form
- [ ] Handle form submission
- [ ] Validate inputs

### Part 5: Navigation & Styling (40 min)
- [ ] Create navigation menu
- [ ] Style with CSS
- [ ] Make responsive
- [ ] Add footer

**Total Time: ~2.5 hours**

## 🎨 Features Checklist

- [ ] Homepage with post listings
- [ ] Individual post pages
- [ ] Create new posts
- [ ] Category filtering
- [ ] Responsive navigation
- [ ] Professional styling
- [ ] Author attribution
- [ ] Timestamps

## 💡 Key Concepts

### Template Inheritance
```python
# base.html
<!DOCTYPE html>
<html>
<head>{% block head %}{% endblock %}</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>

# post.html
{% extends "base.html" %}
{% block content %}
    <h1>{{ post.title }}</h1>
{% endblock %}
```

### Static Files
```python
# Flask automatically serves from static/
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<img src="{{ url_for('static', filename='images/logo.png') }}">
```

### URL Parameters
```python
# Path parameter
@app.route('/post/<int:post_id>')
def view_post(post_id):
    pass

# Query parameter
@app.route('/posts')
def list_posts():
    category = request.args.get('category')
```

## 🎓 What You'll Learn

1. **Template inheritance** - DRY principle for HTML
2. **Static file serving** - CSS, images, JS
3. **Multi-page navigation** - Connected user experience
4. **Responsive design** - Mobile-first layouts
5. **Content management** - Creating and displaying posts

---

**Start coding:** Open `starter/flask_version/app.py`
