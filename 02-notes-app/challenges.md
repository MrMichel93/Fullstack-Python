# Extension Challenges - Notes App

Once you've completed the basic Notes App, try these challenges to practice your skills!

## 🌟 Beginner Challenges

### 1. Add Note Character Count
**Difficulty:** ⭐
**Concepts:** JavaScript basics, DOM manipulation

Show the character count for the content textarea as the user types.

**Hints:**
- Add a `<span id="char-count">0</span>` below the textarea
- Use JavaScript `oninput` event
- `textarea.value.length` gives you the character count

### 2. Empty Note Prevention
**Difficulty:** ⭐
**Concepts:** Form validation, user feedback

Prevent empty or whitespace-only notes from being created.

**Hints:**
- Add validation in the Python route
- Use `str.strip()` to remove whitespace
- Return an error message if empty
- Alternative: Use HTML5 `required` attribute

### 3. Timestamp Formatting
**Difficulty:** ⭐
**Concepts:** Date/time handling

Display timestamps in a more readable format (e.g., "2 hours ago").

**Hints:**
- Install `python-dateutil` or use Python's `datetime`
- Create a helper function
- Use Jinja2 filters in templates

### 4. Color Themes
**Difficulty:** ⭐
**Concepts:** CSS variables, styling

Add a toggle to switch between light and dark mode.

**Hints:**
- Use CSS variables (`:root { --bg-color: white; }`)
- Add a button to toggle a `.dark-mode` class
- Store preference in localStorage

## 🔥 Intermediate Challenges

### 5. Search Functionality
**Difficulty:** ⭐⭐
**Concepts:** Database queries, filtering

Add a search box to filter notes by title or content.

**Hints:**
- Add a search form with GET method
- Use SQL `WHERE title LIKE ? OR content LIKE ?`
- Pass search term: `'%' + search_term + '%'`

### 6. Categories/Tags
**Difficulty:** ⭐⭐
**Concepts:** Database relations, many-to-many

Add categories or tags to organize notes.

**Hints:**
- Create a `categories` table
- Create a `note_categories` junction table
- Update create/edit forms to include category selection
- Add filter by category

### 7. Note Archiving
**Difficulty:** ⭐⭐
**Concepts:** Soft deletes, filtering

Instead of deleting, allow archiving notes (hide but keep).

**Hints:**
- Add `archived` column (BOOLEAN, default FALSE)
- Change delete to set `archived = TRUE`
- Filter out archived notes in main view
- Add "View Archived" page

### 8. Markdown Support
**Difficulty:** ⭐⭐
**Concepts:** Text processing, libraries

Allow notes to be written in Markdown and display formatted.

**Hints:**
- Install `markdown` package: `pip install markdown`
- Convert in template: `{{ note.content | markdown }}`
- Or convert in route before rendering
- Add a preview toggle

## 🚀 Advanced Challenges

### 9. Note Sharing
**Difficulty:** ⭐⭐⭐
**Concepts:** URL generation, permissions

Allow users to generate shareable links for specific notes.

**Hints:**
- Add `share_token` column (unique random string)
- Create route `/share/<token>`
- Add "Generate Share Link" button
- No authentication required for shared links

### 10. Rich Text Editor
**Difficulty:** ⭐⭐⭐
**Concepts:** JavaScript libraries, WYSIWYG

Replace textarea with a rich text editor (bold, italic, lists, etc.).

**Hints:**
- Use a library like Quill.js or TinyMCE
- Include via CDN in base.html
- Initialize on textarea
- Store HTML in database

### 11. Export Notes
**Difficulty:** ⭐⭐⭐
**Concepts:** File generation, HTTP responses

Allow exporting all notes as a text file, JSON, or PDF.

**Hints:**
- Add `/export?format=txt` route
- Use `send_file()` or return file as response
- Set proper headers: `Content-Type`, `Content-Disposition`
- For PDF: use `reportlab` library

### 12. Note Reminders
**Difficulty:** ⭐⭐⭐
**Concepts:** Scheduled tasks, background jobs

Add optional reminder dates to notes.

**Hints:**
- Add `reminder_date` column (TIMESTAMP, nullable)
- Add date input to form
- Show notes with upcoming reminders
- Advanced: Use `APScheduler` for notifications

## 🏆 Expert Challenges

### 13. Full-Text Search
**Difficulty:** ⭐⭐⭐⭐
**Concepts:** SQLite FTS, indexing

Implement fast full-text search using SQLite FTS5.

**Hints:**
- Create virtual table with FTS5
- Sync data between main and FTS table
- Use FTS search syntax
- Highlight matching terms

### 14. Multi-User Support
**Difficulty:** ⭐⭐⭐⭐
**Concepts:** Authentication, sessions, user isolation

Add user registration and login so each user has their own notes.

**Hints:**
- Create `users` table
- Add `user_id` to notes table
- Use Flask-Login extension
- Filter notes by current user
- See Project 4 (Inventory Tracker) for auth example

### 15. Real-Time Collaboration
**Difficulty:** ⭐⭐⭐⭐⭐
**Concepts:** WebSockets, concurrent editing

Allow multiple users to edit the same note simultaneously.

**Hints:**
- Use Flask-SocketIO
- Broadcast changes to all connected clients
- Handle conflict resolution
- Show who's currently viewing/editing

### 16. Mobile App
**Difficulty:** ⭐⭐⭐⭐⭐
**Concepts:** API design, mobile development

Create a REST API and mobile app (React Native, Flutter, etc.).

**Hints:**
- Add JSON API endpoints
- Implement JWT authentication
- Use FastAPI instead of Flask for automatic API docs
- Build mobile app that consumes API

## 💡 Tips for Tackling Challenges

1. **Start Small:** Pick one challenge that interests you
2. **Research First:** Look up the concepts and libraries involved
3. **Break It Down:** Divide the challenge into smaller tasks
4. **Test Incrementally:** Test each part as you build it
5. **Commit Often:** Save your progress with git commits
6. **Ask for Help:** Use documentation, forums, and AI assistants

## 📚 Helpful Resources

- **Flask Documentation:** https://flask.palletsprojects.com/
- **SQLite Documentation:** https://www.sqlite.org/docs.html
- **Jinja2 Templates:** https://jinja.palletsprojects.com/
- **CSS Tricks:** https://css-tricks.com/
- **MDN Web Docs:** https://developer.mozilla.org/

---

**Pick a challenge and start coding!** Remember: the goal is to learn, not to be perfect. 🚀
