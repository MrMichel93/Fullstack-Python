# Practice Problems - Security Basics

This directory contains practice problems to help you master security concepts in Flask applications.

⚠️ **Security Note:** These problems contain intentionally vulnerable code for educational purposes. Never use this code in production!

## Running the Tests

Each problem has a starter file and a test file. To verify your solution:

1. Install dependencies (if you haven't already):
   ```bash
   pip install -r ../../../requirements.txt
   ```

2. Run tests for a specific problem:
   ```bash
   # For Problem 1
   pytest test_problem1.py -v
   
   # For Problem 2
   pytest test_problem2.py -v
   
   # For Problem 3
   pytest test_problem3.py -v
   ```

3. Run all tests:
   ```bash
   pytest -v
   ```

## Problems

### Problem 1: Secure Password Handling
**File:** `problem1_password_hash.py`  
**Tests:** `test_problem1.py`  
**Difficulty:** Medium (25-30 minutes)

Implement secure password hashing and validation using werkzeug.security.

### Problem 2: Prevent Security Vulnerabilities
**File:** `problem2_fix_vulnerabilities.py`  
**Tests:** `test_problem2.py`  
**Difficulty:** Medium (20-25 minutes)

Fix XSS and SQL injection vulnerabilities in provided code.

### Problem 3: Input Validation
**File:** `problem3_input_validation.py`  
**Tests:** `test_problem3.py`  
**Difficulty:** Medium (20-25 minutes)

Implement comprehensive input validation and sanitization.

## Getting Started

1. Read the problem description in the markdown comments at the top of each problem file
2. Complete the TODO sections in the starter code
3. Run the tests to verify your solution
4. All tests should pass when you're done!

## Security Tips

- **Never store passwords in plain text** - Always hash them
- **Use parameterized queries** - Prevent SQL injection
- **Validate all input** - Never trust user data
- **Escape output** - Prevent XSS attacks
- **Use HTTPS** - Encrypt data in transit
- **Keep dependencies updated** - Patch vulnerabilities

## Important Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Flask Security](https://flask.palletsprojects.com/en/latest/security/)
- [Werkzeug Security Utils](https://werkzeug.palletsprojects.com/en/latest/utils/#module-werkzeug.security)
