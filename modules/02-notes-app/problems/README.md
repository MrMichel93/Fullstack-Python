# Practice Problems - Notes App

This directory contains practice problems to help you master CRUD operations and database handling.

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

### Problem 1: Basic CRUD Notes App
**File:** `problem1_crud_notes.py`  
**Tests:** `test_problem1.py`  
**Difficulty:** Medium (30-40 minutes)

Create a complete CRUD application with SQLite database for managing notes.

### Problem 2: Notes with Categories
**File:** `problem2_categories.py`  
**Tests:** `test_problem2.py`  
**Difficulty:** Medium (30-40 minutes)

Extend the notes app to support categories and filtering.

### Problem 3: Notes with Search
**File:** `problem3_search.py`  
**Tests:** `test_problem3.py`  
**Difficulty:** Hard (40-50 minutes)

Add search functionality with SQL LIKE queries.

## Getting Started

1. Read the problem description in the markdown comments at the top of each problem file
2. Complete the TODO sections in the starter code
3. Run the tests to verify your solution
4. All tests should pass when you're done!

## Tips

- Read the test file to understand what's expected
- Use SQLite documentation: https://www.sqlitetutorial.net/
- Always use parameterized queries to prevent SQL injection
- Remember to commit your database changes with `db.commit()`
- Close database connections with `db.close()` when done
- Run tests frequently to catch issues early

## Database Setup

Each problem will need a database. The test files will use an in-memory database (`:memory:`), so you don't need to worry about cleaning up test data.

For manual testing, your app will create a `notes.db` file in the problems directory.
