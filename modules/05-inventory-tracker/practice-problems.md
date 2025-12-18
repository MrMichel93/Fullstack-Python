# Practice Problems - Inventory Tracker

Before moving on, practice these exercises to master user authentication:

## Problem 1: User Registration & Login
**Difficulty:** Medium  
**Time:** 40-50 minutes

Create a user authentication system:
- Registration form with username, email, password
- Hash passwords using Werkzeug
- Login form to verify credentials
- Store user ID in session after login
- Logout functionality to clear session
- Flash messages for feedback
- Database with users table (id, username, email, password, created_at)

**What you'll practice:**
- Password hashing and verification
- Session management
- User registration flow
- Login/logout functionality

---

## Problem 2: Protected Inventory System
**Difficulty:** Hard  
**Time:** 50-60 minutes

Build an inventory tracker with authentication:
- Only logged-in users can access inventory
- Create `login_required` decorator
- Each user has their own inventory items
- CRUD operations for items (name, quantity, price, category)
- Dashboard showing user's inventory statistics
- User can only see/edit their own items
- Proper error handling and flash messages

**What you'll practice:**
- Protected routes with decorators
- User-specific data isolation
- Authorization (users can only access their data)
- Complete authenticated CRUD application

---

## Problem 3: Advanced User Features
**Difficulty:** Hard  
**Time:** 50-60 minutes

Add advanced features to your inventory app:
- Password strength validation (min 8 chars, uppercase, number)
- Email validation
- "Remember me" functionality
- Profile page where users can update info
- Change password feature (verify old password)
- Low stock alerts (items below threshold)
- Export inventory to CSV
- User dashboard with statistics and charts

**What you'll practice:**
- Input validation
- Password changing workflow
- Advanced session features
- Data export
- User experience improvements

**Bonus Challenge:**
- Password reset via email
- Two-factor authentication (2FA)
- User roles (admin, regular user)
- Item sharing between users

---

## 📝 Practice Problems Now Available as Code!

### How to Use

1. Navigate to the `problems/` directory:
   ```bash
   cd modules/05-inventory-tracker/problems/
   ```

2. Read the problem description in each Python file
3. Complete the TODO sections
4. Run tests to verify your solution:
   ```bash
   pytest test_problem1.py -v
   pytest test_problem2.py -v
   pytest test_problem3.py -v
   ```

### Available Files

- **Problem 1:** `problem1_auth_system.py` + `test_problem1.py`
- **Problem 2:** `problem2_protected_inventory.py` + `test_problem2.py`
- **Problem 3:** `problem3_advanced_features.py` + `test_problem3.py`

See `problems/README.md` for detailed instructions!

---

## Next Steps

After completing these practice problems:

1. ✅ You can implement secure authentication
2. ✅ You understand session management
3. ✅ You can protect routes and data
4. ✅ You know how to validate user input

**Continue to:** [Security Basics](../06-security-basics/) and [Debugging & Testing](../07-debugging-testing/)
