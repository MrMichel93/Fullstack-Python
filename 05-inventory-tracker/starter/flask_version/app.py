"""
Inventory Tracker - Flask Version (Starter)
Multi-user inventory management with authentication

Learning objectives:
- User authentication (register, login, logout)
- Password hashing
- Sessions
- Protected routes
- User-specific data
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
# NOTE: In production, use a fixed secret key from environment variables
# For development/learning, this is acceptable
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
DATABASE = 'inventory.db'


def get_db():
    """Create a database connection"""
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def init_db():
    """Initialize the database"""
    db = get_db()
    
    # TODO: Create users table
    # Columns: id, username, email, password_hash, created_at
    
    # TODO: Create products table
    # Columns: id, name, quantity, price, user_id, created_at
    # Foreign key: user_id references users(id)
    
    db.commit()
    db.close()


def login_required(f):
    """Decorator to require login for routes"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login first', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    """Landing page"""
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration"""
    if request.method == 'POST':
        # TODO: Get form data
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # TODO: Validate inputs
        
        # TODO: Hash password
        # password_hash = generate_password_hash(password)
        
        # TODO: Save user to database
        
        # TODO: Login user and redirect
        # session['user_id'] = user_id
        
        return redirect(url_for('dashboard'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login"""
    if request.method == 'POST':
        # TODO: Get credentials
        username = request.form.get('username')
        password = request.form.get('password')
        
        # TODO: Find user in database
        
        # TODO: Verify password
        # if check_password_hash(user['password_hash'], password):
        
        # TODO: Create session
        # session['user_id'] = user['id']
        
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    """User logout"""
    session.clear()
    flash('Logged out successfully', 'success')
    return redirect(url_for('index'))


@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard with products"""
    db = get_db()
    
    # TODO: Fetch user's products
    # Filter by session['user_id']
    products = []
    
    db.close()
    return render_template('dashboard.html', products=products)


@app.route('/products/add', methods=['GET', 'POST'])
@login_required
def add_product():
    """Add a new product"""
    if request.method == 'POST':
        # TODO: Get form data
        name = request.form.get('name')
        quantity = request.form.get('quantity')
        price = request.form.get('price')
        
        # TODO: Save with user_id from session
        
        return redirect(url_for('dashboard'))
    
    return render_template('add_product.html')


if __name__ == '__main__':
    init_db()
    print("📦 Inventory Tracker is running!")
    print("🔒 Open http://localhost:5000")
    app.run(debug=True, port=5000)
