# Project 1: Notes App

## 📝 What You'll Build
A simple note-taking web application where users can:
- Create new notes
- View all notes
- Edit existing notes
- Delete notes

## 🎯 Learning Objectives

### Backend Concepts
- **CRUD Operations** (Create, Read, Update, Delete)
- **Database connections** with SQLite
- **Form handling** with POST requests
- **Basic routing** in Flask/FastAPI

### Frontend Concepts
- **HTML Forms** for user input
- **Dynamic content** rendering with templates
- **Links and navigation**
- **Basic styling** with CSS

## 🛠️ Tech Stack
- **Backend:** Flask or FastAPI
- **Database:** SQLite
- **Frontend:** HTML + CSS (no JavaScript needed)

## 📂 Project Structure

```
02-notes-app/
├── README.md (this file)
├── challenges.md (extension ideas)
├── starter/
│   ├── flask_version/
│   │   ├── app.py (TODO: Complete the TODOs)
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── index.html (TODO: Complete the TODOs)
│   │   │   └── edit.html (TODO: Complete the TODOs)
│   │   └── static/
│   │       └── style.css
│   └── fastapi_version/
│       ├── app.py (TODO: Complete the TODOs)
│       └── templates/
│           ├── base.html
│           ├── index.html (TODO: Complete the TODOs)
│           └── edit.html (TODO: Complete the TODOs)
└── solution/
    ├── flask_version/ (complete working code)
    └── fastapi_version/ (complete working code)
```

## 🚀 Getting Started

### 1. Choose Your Framework

Pick **Flask** OR **FastAPI** (both do the same thing):

- **Flask:** Simpler, fewer concepts, great for beginners
- **FastAPI:** Modern, automatic API docs, slightly more complex

### 2. Install Dependencies

```bash
cd 02-notes-app/starter/flask_version
# or
cd 02-notes-app/starter/fastapi_version

# Install requirements
pip install -r requirements.txt
```

### 3. Run the Starter App

```bash
# Flask
python app.py

# FastAPI
uvicorn app:app --reload
```

Visit `http://localhost:5000` (Flask) or `http://localhost:8000` (FastAPI)

## ✅ TODO Checklist

Work through these steps in order:

### Part 1: Setup & Database (30 min)
- [ ] Read through `app.py` to understand the structure
- [ ] Complete `init_db()` function to create the notes table
- [ ] Test: Run the app - it should start without errors

### Part 2: Create Notes (30 min)
- [ ] Complete the `create_note()` route to handle form submissions
- [ ] Complete the form in `index.html` 
- [ ] Test: Submit a note and verify it's saved (check database)

### Part 3: View Notes (20 min)
- [ ] Complete the `index()` route to fetch all notes
- [ ] Complete the display section in `index.html` to show notes
- [ ] Test: Refresh page - you should see your notes

### Part 4: Edit Notes (40 min)
- [ ] Complete the `edit_note()` route (GET request)
- [ ] Complete the `update_note()` route (POST request)
- [ ] Complete `edit.html` form
- [ ] Test: Click edit, change a note, save

### Part 5: Delete Notes (20 min)
- [ ] Complete the `delete_note()` route
- [ ] Add delete button in `index.html`
- [ ] Test: Delete a note

### Part 6: Styling (20 min)
- [ ] Review `style.css` and customize colors
- [ ] Add your own styling touches
- [ ] Test: App should look clean and organized

**Total Time: ~2.5 hours**

## 🧪 Testing Your App

1. **Create Test:**
   - Submit a new note
   - Check it appears in the list
   - Verify it's in the database

2. **Read Test:**
   - Refresh the page
   - All notes should display
   - Try with 5+ notes

3. **Update Test:**
   - Click edit on a note
   - Modify the content
   - Save and verify changes appear

4. **Delete Test:**
   - Click delete on a note
   - Confirm it's removed from list
   - Verify it's gone from database

5. **Edge Cases:**
   - Try submitting empty notes
   - Test with very long content
   - Edit then cancel (use back button)

## 📊 Database Schema

```sql
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Fields:**
- `id`: Unique identifier (auto-generated)
- `title`: Note title/subject
- `content`: Main note text
- `created_at`: When note was created

## 🎨 Features Checklist

- [ ] Create a new note with title and content
- [ ] View all notes on the home page
- [ ] Edit existing notes
- [ ] Delete notes
- [ ] Display creation timestamp
- [ ] Basic styling with CSS
- [ ] Form validation (no empty notes)

## 🐛 Common Issues & Solutions

### Database doesn't exist
```bash
# Delete old database and restart
rm notes.db
python app.py
```

### Changes don't appear
- Did you commit to database? (`db.commit()`)
- Are you redirecting after POST? (`redirect()`)
- Is the database file in the right location?

### Forms not submitting
- Check form `action` attribute matches route
- Verify `method="POST"` in form tag
- Ensure input fields have `name` attributes

### Template not found
- Templates must be in `templates/` folder
- Check filename spelling exactly
- Use `render_template('filename.html')`

## 💡 Understanding the Code

### Flask Route Example
```python
@app.route('/notes', methods=['POST'])
def create_note():
    # Get form data
    title = request.form['title']
    content = request.form['content']
    
    # Save to database
    db.execute("INSERT INTO notes (title, content) VALUES (?, ?)",
               (title, content))
    db.commit()
    
    # Redirect to home
    return redirect('/')
```

### SQLite Commands
```python
# Query (SELECT)
notes = db.execute("SELECT * FROM notes").fetchall()

# Insert
db.execute("INSERT INTO notes (title, content) VALUES (?, ?)", 
           (title, content))
db.commit()

# Update
db.execute("UPDATE notes SET title=?, content=? WHERE id=?",
           (title, content, note_id))
db.commit()

# Delete
db.execute("DELETE FROM notes WHERE id=?", (note_id,))
db.commit()
```

## 🎓 Key Concepts Review

After completing this project, you should understand:

1. **CRUD Pattern:** Create, Read, Update, Delete - the foundation of most web apps
2. **Forms:** How to send data from browser to server
3. **Templates:** Mixing HTML with dynamic Python data
4. **Routing:** Mapping URLs to Python functions
5. **Database:** Storing and retrieving persistent data
6. **HTTP Methods:** GET for viewing, POST for submitting

## 📚 Next Steps

Once you complete this project:

1. ✅ Review the solution code if you got stuck
2. ✅ Try the [Extension Challenges](./challenges.md)
3. ✅ Move to **[URL Shortener](../03-url-shortener/)** project

## 🏆 Extension Ideas

Want more practice? See [challenges.md](./challenges.md) for ideas like:
- Add categories/tags to notes
- Search functionality
- Note archiving
- Markdown support
- Export notes to text file

---

**Ready to code?** Open `starter/flask_version/app.py` or `starter/fastapi_version/app.py` and start with the first TODO!
