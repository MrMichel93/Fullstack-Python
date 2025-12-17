# Project 4: Inventory Tracker

## 📦 What You'll Build
An inventory management system with authentication where users can:
- Register and login
- Track products (name, quantity, price)
- Update stock levels
- View low-stock alerts
- Manage their own inventory

## 🎯 Learning Objectives

### Backend Concepts
- **User authentication** - Registration, login, logout
- **Sessions** - Keeping users logged in
- **Authorization** - Protecting routes
- **Data validation** - Server-side input checking

### Frontend Concepts
- **Login/Registration forms** - User account management
- **Protected pages** - Content only for logged-in users
- **Flash messages** - User feedback
- **Data tables** - Organized information display

## 🛠️ Tech Stack
- **Backend:** Flask with Flask-Login
- **Database:** SQLite (users + products tables)
- **Frontend:** HTML + CSS

## 📂 Project Structure

```
05-inventory-tracker/
├── README.md
├── challenges.md
├── starter/
│   └── flask_version/
│       ├── app.py
│       ├── templates/
│       │   ├── base.html
│       │   ├── login.html
│       │   ├── register.html
│       │   ├── dashboard.html
│       │   └── add_product.html
│       └── static/
│           └── style.css
└── solution/
    └── flask_version/
```

## ✅ TODO Checklist

### Part 1: Database Setup (30 min)
- [ ] Create users table (id, username, password_hash, email)
- [ ] Create products table (id, name, quantity, price, user_id)
- [ ] Set up foreign keys

### Part 2: User Registration (40 min)
- [ ] Build registration form
- [ ] Validate inputs (username, email, password)
- [ ] Hash passwords (werkzeug.security)
- [ ] Save to database

### Part 3: User Login (30 min)
- [ ] Build login form
- [ ] Verify credentials
- [ ] Create session
- [ ] Implement logout

### Part 4: Protected Routes (30 min)
- [ ] Add login_required decorator
- [ ] Redirect unauthorized users
- [ ] Show user-specific data

### Part 5: Inventory Management (50 min)
- [ ] Display user's products
- [ ] Add new products
- [ ] Update quantities
- [ ] Delete products
- [ ] Show low-stock warnings

**Total Time: ~3 hours**

## 🔒 Security Features

### Password Hashing
```python
from werkzeug.security import generate_password_hash, check_password_hash

# On registration
hashed = generate_password_hash(password)

# On login
if check_password_hash(user.password_hash, password):
    # Login successful
```

### Session Management
```python
from flask_login import LoginManager, login_user, logout_user, login_required

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/dashboard')
@login_required  # Requires authentication
def dashboard():
    pass
```

## 🎨 Features Checklist

- [ ] User registration with validation
- [ ] Secure login/logout
- [ ] Password hashing
- [ ] Session management
- [ ] Add products
- [ ] Edit quantities
- [ ] Delete products
- [ ] Low-stock alerts (<10 items)
- [ ] User-specific data isolation
- [ ] Flash messages for feedback

## 💡 Key Concepts

### Authentication Flow
```
Registration → Hash Password → Save User
Login → Verify Password → Create Session
Protected Route → Check Session → Allow/Deny Access
```

### Data Isolation
```python
# Users only see their own products
@app.route('/products')
@login_required
def products():
    products = db.execute(
        "SELECT * FROM products WHERE user_id = ?",
        (current_user.id,)
    ).fetchall()
```

## 🎓 What You'll Learn

1. **User authentication** - Secure registration and login
2. **Password security** - Hashing and verification
3. **Sessions** - Maintaining logged-in state
4. **Authorization** - Protecting routes and data
5. **Data isolation** - Multi-user applications

---

**Start coding:** Open `starter/flask_version/app.py`
