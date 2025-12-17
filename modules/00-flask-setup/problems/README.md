# Practice Problems - Flask Setup

This directory contains practice problems to help you master Flask basics.

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

### Problem 1: Personal Portfolio Page
**File:** `problem1_portfolio.py`  
**Tests:** `test_problem1.py`  
**Difficulty:** Easy (15-20 minutes)

Create a Flask application with home, about, and contact pages using template inheritance.

### Problem 2: Dynamic Greeting App
**File:** `problem2_greeting.py`  
**Tests:** `test_problem2.py`  
**Difficulty:** Easy (15-20 minutes)

Create a Flask application with dynamic routes and query parameters for personalized greetings.

### Problem 3: Simple Form Handler
**File:** `problem3_form.py`  
**Tests:** `test_problem3.py`  
**Difficulty:** Medium (20-30 minutes)

Create a Flask application with form handling, validation, flash messages, and redirects.

## Getting Started

1. Read the problem description in the markdown comments at the top of each problem file
2. Complete the TODO sections in the starter code
3. Run the tests to verify your solution
4. All tests should pass when you're done!

## Tips

- Read the test file to understand what's expected
- Use Flask documentation: https://flask.palletsprojects.com/
- Start simple and build incrementally
- Run tests frequently to catch issues early
