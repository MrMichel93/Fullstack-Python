# Practice Problems - Architecture Primer

This directory contains practice problems to test your understanding of web architecture.

## Running the Tests

Each problem has a Python file where you complete functions, and a test file to verify your understanding.

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

### Problem 1: Trace the Request Journey
**File:** `problem1_request_journey.py`  
**Tests:** `test_problem1.py`  
**Difficulty:** Easy (10-15 minutes)

Write functions that describe what happens during a web request journey.

### Problem 2: Design a URL Structure
**File:** `problem2_url_design.py`  
**Tests:** `test_problem2.py`  
**Difficulty:** Easy (10-15 minutes)

Design appropriate URLs and HTTP methods for blog application operations.

### Problem 3: Debug the Architecture
**File:** `problem3_debug_code.py`  
**Tests:** `test_problem3.py`  
**Difficulty:** Medium (15-20 minutes)

Fix common architecture and Flask routing bugs in provided code.

## Getting Started

1. Read the problem description in the markdown comments at the top of each problem file
2. Complete the TODO sections in the starter code
3. Run the tests to verify your solution
4. All tests should pass when you're done!

## Tips

- Think about the request/response cycle
- Consider HTTP methods and their purposes
- Understand when to use GET vs POST
- Remember proper error handling
