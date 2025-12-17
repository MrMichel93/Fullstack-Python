# Getting Started Guide

Welcome to **Full-Stack Development with Python**! This guide will help you set up your development environment and start building projects.

## 📋 Prerequisites

Before you begin, make sure you have:

- **Python 3.8 or higher** installed
- **Text editor or IDE** (VS Code, PyCharm, or Sublime Text)
- **Web browser** (Chrome, Firefox, or Edge)
- **Basic Python knowledge** (variables, functions, loops)
- **Basic HTML knowledge** (tags, forms)

## 🔧 Installation

### 1. Check Python Version

```bash
python --version
# or
python3 --version
```

You should see `Python 3.8.x` or higher.

### 2. Clone the Repository

```bash
git clone https://github.com/MrMichel93/Fullstack-Python.git
cd Fullstack-Python
```

### 3. Create a Virtual Environment (Recommended)

**Why?** Virtual environments keep project dependencies isolated.

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You'll see `(venv)` in your terminal when activated.

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs Flask and other necessary packages.

## 🚀 Running Your First Project

### Start with the Architecture Primer

1. Read the [Architecture Primer](./01-architecture-primer/README.md) to understand web app basics
2. It covers:
   - Client vs Server
   - Request/Response lifecycle
   - How data flows through web apps

### Run the Notes App

Let's test your setup with the complete solution:

```bash
cd 02-notes-app/solution/flask_version
python app.py
```

You should see:
```
🚀 Notes App is running!
📝 Open http://localhost:5000 in your browser
```

**Open your browser** and visit `http://localhost:5000`

Try:
- Creating a note
- Editing a note
- Deleting a note

Press `Ctrl+C` in the terminal to stop the server.

## 📚 Learning Path

### Recommended Order

1. **[Architecture Primer](./01-architecture-primer/)** - Start here! (30 min)
   - Understand web fundamentals before coding

2. **[Notes App](./02-notes-app/)** - Your first project (2-3 hours)
   - Start with `starter/flask_version/`
   - Follow TODOs in the code
   - Check solution if stuck

3. **[URL Shortener](./03-url-shortener/)** - Build on what you learned (2-3 hours)
   - New concepts: redirects, URL generation
   - Practice database queries

4. **[Simple Blog](./04-simple-blog/)** - Multi-page app (2-3 hours)
   - Template inheritance
   - Static files
   - Navigation

5. **[Inventory Tracker](./05-inventory-tracker/)** - Add authentication (3-4 hours)
   - User registration/login
   - Password security
   - Protected routes

6. **[Security Basics](./06-security-basics/)** - Essential reading
   - Read before building your own apps
   - Covers common vulnerabilities

7. **[Debugging & Testing](./07-debugging-testing/)** - Reference guide
   - Use when you get stuck
   - Learn debugging techniques

## 🛠️ Development Workflow

### For Each Project:

1. **Read the README** - Understand what you're building
2. **Open starter code** - Navigate to `starter/flask_version/`
3. **Follow TODOs** - Search for `TODO` comments in code
4. **Test frequently** - Run the app after each feature
5. **Check solution** - Compare with `solution/` if stuck
6. **Try challenges** - Extend the project with `challenges.md`

### Example: Starting Notes App

```bash
cd 02-notes-app/starter/flask_version
code .  # Opens VS Code (or use your editor)
python app.py  # Run the app
```

### Tips

- **Read error messages carefully** - They tell you what's wrong
- **Use print debugging** - Add `print()` statements to understand code flow
- **Check the database** - Use DB Browser for SQLite to view data
- **Commit often** - Use git to save your progress
- **Take breaks** - Fresh eyes find bugs faster

## 🐛 Troubleshooting

### "Module not found" Error

**Problem:** `ModuleNotFoundError: No module named 'flask'`

**Solution:** Make sure you:
1. Activated virtual environment: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
2. Installed requirements: `pip install -r requirements.txt`

### Port Already in Use

**Problem:** `Address already in use`

**Solution:** 
- Another app is using port 5000
- Stop the other app or change port:
  ```python
  app.run(debug=True, port=5001)  # Use different port
  ```

### Database Locked

**Problem:** `database is locked`

**Solution:**
- Close all database connections in your code
- Delete `notes.db` and restart the app
- Use proper `try/finally` blocks to close connections

### Template Not Found

**Problem:** `jinja2.exceptions.TemplateNotFound`

**Solution:**
- Check that `templates/` folder exists
- Verify filename spelling exactly matches
- Make sure you're in the correct directory

### Changes Not Appearing

**Problem:** Code changes don't show up

**Solution:**
- Make sure debug mode is on: `app.run(debug=True)`
- Do a hard refresh: `Ctrl+F5` (or `Cmd+Shift+R` on Mac)
- Check you're editing the right file
- Restart the Flask server

## 💡 Helpful Tools

### Text Editors / IDEs

- **VS Code** (recommended for beginners)
  - Free and lightweight
  - Great Python extensions
  - Integrated terminal

- **PyCharm** (full-featured IDE)
  - Professional Python IDE
  - More features, steeper learning curve

### Database Tools

- **DB Browser for SQLite**
  - Visual database browser
  - View and edit database contents
  - Download: https://sqlitebrowser.org/

### Browser Tools

- **Chrome DevTools** / **Firefox Developer Tools**
  - Press `F12` in browser
  - View HTML, CSS, Network requests
  - Debug JavaScript

## 📖 Additional Resources

### Python
- Official Tutorial: https://docs.python.org/3/tutorial/
- Real Python: https://realpython.com/
- Python Tutor (visualize code): http://pythontutor.com/

### Flask
- Official Docs: https://flask.palletsprojects.com/
- Flask Mega-Tutorial: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

### HTML/CSS
- MDN Web Docs: https://developer.mozilla.org/
- W3Schools: https://www.w3schools.com/
- CSS Tricks: https://css-tricks.com/

### SQL
- SQLite Tutorial: https://www.sqlitetutorial.net/
- SQL Zoo: https://sqlzoo.net/

## 🎯 What to Do If You're Stuck

1. **Read the error message** - It usually tells you what's wrong
2. **Check the README** - Project-specific help
3. **Review the solution** - Compare your code
4. **Use debugging guide** - See `07-debugging-testing/`
5. **Search online** - Stack Overflow, documentation
6. **Ask for help** - GitHub issues, forums, study groups

## ✅ Checklist

Before starting projects:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Ran Notes App solution successfully
- [ ] Read Architecture Primer
- [ ] Text editor ready
- [ ] Browser open

## 🚀 Ready to Start!

You're all set! Head to the [Architecture Primer](./01-architecture-primer/) to begin your journey.

**Remember:** Learning to code is a marathon, not a sprint. Take your time, practice regularly, and don't be afraid to make mistakes. That's how you learn!

Happy coding! 🎉

---

**Need help?** Open an issue on GitHub or check the [Debugging & Testing guide](./07-debugging-testing/).
