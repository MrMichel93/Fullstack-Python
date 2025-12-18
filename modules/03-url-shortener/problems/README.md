# Practice Problems - URL Shortener

This directory contains practice problems to help you master redirects and unique ID generation.

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

### Problem 1: Basic URL Shortener
**File:** `problem1_basic_shortener.py`  
**Tests:** `test_problem1.py`  
**Difficulty:** Medium (30-40 minutes)

Create a basic URL shortening service with random code generation and redirects.

### Problem 2: URL Shortener with Click Tracking
**File:** `problem2_click_tracking.py`  
**Tests:** `test_problem2.py`  
**Difficulty:** Medium (30-40 minutes)

Add click tracking and statistics to your URL shortener.

### Problem 3: URL Shortener with Copy Feature
**File:** `problem3_copy_feature.py`  
**Tests:** `test_problem3.py`  
**Difficulty:** Medium (30-40 minutes)

Add frontend features like copy to clipboard and URL validation.

## Getting Started

1. Read the problem description in the markdown comments at the top of each problem file
2. Complete the TODO sections in the starter code
3. Run the tests to verify your solution
4. All tests should pass when you're done!

## Tips

- Use `string.ascii_letters + string.digits` for generating random codes
- Use 302 redirects (temporary) for URL shorteners
- Always validate URLs before storing them
- Use parameterized queries to prevent SQL injection
- Remember to commit database changes with `db.commit()`
- Test your redirects manually by visiting the short URLs
