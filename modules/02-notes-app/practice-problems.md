# Practice Problems - Notes App

Before moving on, practice these exercises to solidify your CRUD and database knowledge:

## Problem 1: Basic CRUD Notes App
**Difficulty:** Medium  
**Time:** 30-40 minutes

Create a Flask application with complete CRUD functionality for notes:
- Display all notes on the home page (`/`)
- Create a new note with a form (`/notes/new` GET to show form, POST to `/notes` to create)
- View a single note (`/notes/<id>`)
- Edit a note (`/notes/<id>/edit` GET to show form, POST to `/notes/<id>/update` to update)
- Delete a note (POST to `/notes/<id>/delete`)
- Use SQLite database with a `notes` table (id, title, content, created_at)

**What you'll practice:**
- All four CRUD operations
- Database queries (INSERT, SELECT, UPDATE, DELETE)
- Form handling with GET and POST methods
- Dynamic routing with parameters

---

## Problem 2: Notes with Categories
**Difficulty:** Medium  
**Time:** 30-40 minutes

Extend the basic notes app to support categories:
- Add a `category` field to the notes table (e.g., "Work", "Personal", "Ideas")
- Display notes grouped by category on the home page
- Add a filter to show notes from a specific category (`/notes?category=Work`)
- Show a category dropdown in the create/edit forms
- Display a count of notes in each category

**What you'll practice:**
- More complex SQL queries with WHERE clauses
- URL query parameters with `request.args`
- Grouping and filtering data
- Working with multiple database fields

---

## Problem 3: Notes with Search
**Difficulty:** Hard  
**Time:** 40-50 minutes

Add search functionality to your notes app:
- Add a search form on the home page
- Search notes by title and content (`/notes/search?q=keyword`)
- Highlight search terms in results
- Show "No results found" message when appropriate
- Display search results count
- Keep the search query in the search box after searching

**What you'll practice:**
- SQL LIKE queries for text search
- Working with query parameters
- Conditional rendering in templates
- User experience improvements

**Bonus Challenge:**
- Add pagination (10 notes per page)
- Sort notes by date (newest/oldest first)
- Add tags to notes (many-to-many relationship)
- Export notes to JSON format

---

## 📝 Practice Problems Now Available as Code!

**NEW:** These practice problems are now available as individual Python files with automated tests!

### How to Use

1. Navigate to the `problems/` directory:
   ```bash
   cd modules/02-notes-app/problems/
   ```

2. Read the problem description in each Python file
3. Complete the TODO sections
4. Run tests to verify your solution:
   ```bash
   pytest test_problem1.py -v  # For Problem 1
   pytest test_problem2.py -v  # For Problem 2
   pytest test_problem3.py -v  # For Problem 3
   ```

### Available Files

- **Problem 1:** `problem1_crud_notes.py` + `test_problem1.py`
- **Problem 2:** `problem2_categories.py` + `test_problem2.py`
- **Problem 3:** `problem3_search.py` + `test_problem3.py`

See `problems/README.md` for detailed instructions!

---

## Next Steps

After completing these practice problems:

1. ✅ You can perform full CRUD operations
2. ✅ You understand database queries
3. ✅ You can handle complex forms
4. ✅ You know how to search and filter data

**Continue to:** [URL Shortener](../03-url-shortener/) to learn about redirects and ID generation.
