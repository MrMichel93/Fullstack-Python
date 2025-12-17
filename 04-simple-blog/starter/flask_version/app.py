"""
Simple Blog - Flask Version (Starter)
A multi-page blog with categories and posts

Learning objectives:
- Multi-page routing
- Template inheritance
- Static files
- Categories and filtering
"""

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'blog.db'


def get_db():
    """Create a database connection"""
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def init_db():
    """Initialize the database"""
    db = get_db()
    
    # TODO: Create posts table
    # Columns: id, title, content, category, author, created_at
    
    # TODO: Create sample posts for testing
    
    db.commit()
    db.close()


@app.route('/')
def home():
    """Display all blog posts"""
    db = get_db()
    
    # TODO: Fetch all posts, ordered by newest first
    posts = []
    
    db.close()
    return render_template('home.html', posts=posts)


@app.route('/post/<int:post_id>')
def view_post(post_id):
    """Display a single post"""
    db = get_db()
    
    # TODO: Fetch the post by ID
    post = None
    
    db.close()
    
    if post is None:
        return "Post not found", 404
    
    return render_template('post.html', post=post)


@app.route('/category/<category>')
def category_posts(category):
    """Display posts from a specific category"""
    db = get_db()
    
    # TODO: Fetch posts in this category
    posts = []
    
    db.close()
    return render_template('category.html', posts=posts, category=category)


@app.route('/create', methods=['GET', 'POST'])
def create_post():
    """Create a new blog post"""
    if request.method == 'POST':
        # TODO: Get form data
        title = request.form.get('title')
        content = request.form.get('content')
        category = request.form.get('category')
        author = request.form.get('author', 'Anonymous')
        
        # TODO: Save to database
        
        return redirect(url_for('home'))
    
    return render_template('create.html')


if __name__ == '__main__':
    init_db()
    print("📰 Simple Blog is running!")
    print("🌐 Open http://localhost:5000")
    app.run(debug=True, port=5000)
