# Practice Problems - Debugging & Testing

This directory contains practice problems to help you master debugging and testing skills.

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

### Problem 1: Add Logging to an Application
**File:** `problem1_logging.py`  
**Tests:** `test_problem1.py`  
**Difficulty:** Easy (20-25 minutes)

Configure Python logging with appropriate log levels for different events.

### Problem 2: Debug the Broken Application
**File:** `problem2_debug_bugs.py`  
**Tests:** `test_problem2.py`  
**Difficulty:** Medium (25-30 minutes)

Find and fix bugs in a Flask application using debugging techniques.

### Problem 3: Write Unit Tests
**File:** `problem3_calculator.py` (provided - working code)  
**Tests:** `test_problem3.py` (you write these)  
**Difficulty:** Medium (30-35 minutes)

Write comprehensive unit tests for a Flask calculator application.

## Getting Started

1. Read the problem description in the markdown comments at the top of each problem file
2. Complete the TODO sections in the starter code
3. Run the tests to verify your solution
4. All tests should pass when you're done!

## Debugging Tips

- Use logging instead of print statements
- Learn to use the Python debugger (pdb)
- Read error messages carefully
- Test edge cases and error conditions
- Handle errors gracefully with try-except

## Testing Tips

- Test both happy path and error cases
- Use fixtures for setup and teardown
- Keep tests independent of each other
- Test one thing at a time
- Use descriptive test names
