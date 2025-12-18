# Practice Problems - Inventory Tracker

This directory contains practice problems to help you master user authentication and session management.

## Running the Tests

1. Install dependencies:
   ```bash
   pip install -r ../../../requirements.txt
   ```

2. Run tests for a specific problem:
   ```bash
   pytest test_problem1.py -v
   pytest test_problem2.py -v
   pytest test_problem3.py -v
   ```

3. Run all tests:
   ```bash
   pytest -v
   ```

## Problems

### Problem 1: User Registration & Login
**Difficulty:** Medium (40-50 minutes)
Implement basic user authentication with registration and login.

### Problem 2: Protected Inventory System
**Difficulty:** Hard (50-60 minutes)
Build a complete inventory system with authentication and user-specific data.

### Problem 3: Advanced User Features
**Difficulty:** Hard (50-60 minutes)
Add advanced features like password validation, profile updates, and more.

## Security Tips

- **NEVER** store passwords in plain text
- Always use `generate_password_hash()` for passwords
- Use `check_password_hash()` to verify passwords
- Set a strong `app.secret_key` for sessions
- Validate all user input before processing
- Use `@login_required` decorator to protect routes
- Always use parameterized queries for database operations

## Database Schema Examples

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Items Table (with user_id)
```sql
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL,
    category TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
```
