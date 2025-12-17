# Projects - Full Stack Flask Applications

This folder contains hands-on projects where you'll build real web applications using Flask. Each project is designed to test and apply your Flask knowledge.

## 📋 Purpose

The projects in this folder are practical exercises that allow you to:
- Apply Flask concepts you learned in the [modules](../modules/) section
- Build full-stack web applications from scratch
- Practice CRUD operations, routing, templates, and more
- Test your understanding of Flask and web development

## 🎯 Project Structure

Each project includes:

1. **README.md** - Project overview, learning objectives, and instructions
2. **starter/** - Starting code with TODOs for you to complete
3. **solution/** - Complete working solution (check when stuck)
4. **challenges.md** - Extension ideas to practice further

## 📚 Available Projects

Work through these projects in order:

### 1. [Notes App](./02-notes-app/)
**Difficulty:** Beginner  
**Time:** 2-3 hours

Learn the fundamentals:
- CRUD operations (Create, Read, Update, Delete)
- Database operations with SQLite
- Form handling
- Basic routing

**What you'll build:** A note-taking application where users can create, view, edit, and delete notes.

---

### 2. [URL Shortener](./03-url-shortener/)
**Difficulty:** Beginner-Intermediate  
**Time:** 2-3 hours

Master routing and redirects:
- URL generation with random strings
- HTTP redirects
- Dynamic routing with parameters
- Click tracking

**What you'll build:** A URL shortening service like bit.ly with click statistics.

---

### 3. [Simple Blog](./04-simple-blog/)
**Difficulty:** Intermediate  
**Time:** 2-3 hours

Work with templates and styling:
- Multi-page routing
- Template inheritance
- Static file serving (CSS, images)
- Navigation menus

**What you'll build:** A blog with posts, categories, and styled pages.

---

### 4. [Inventory Tracker](./05-inventory-tracker/)
**Difficulty:** Intermediate-Advanced  
**Time:** 3-4 hours

Implement authentication:
- User registration and login
- Password hashing
- Session management
- Protected routes
- User-specific data

**What you'll build:** A multi-user inventory management system with secure authentication.

---

## 🚀 How to Use These Projects

### Step 1: Read the Module Content First
Before starting projects, make sure you've read:
- [Flask Setup](../modules/00-flask-setup/) - Install Flask and learn basics
- [Architecture Primer](../modules/01-architecture-primer/) - Understand web fundamentals

### Step 2: Start with the Starter Code
Navigate to each project's `starter/` folder:
```bash
cd 02-notes-app/starter/flask_version
```

### Step 3: Follow the TODOs
Open the code files and look for `TODO` comments. These guide you through completing the project.

Example:
```python
# TODO: Create the notes table
# Hint: Use CREATE TABLE IF NOT EXISTS
# Table should have: id, title, content, created_at
```

### Step 4: Test Your Work
Run your application frequently to test:
```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

### Step 5: Check the Solution When Stuck
If you get stuck, check the `solution/` folder for reference. Compare your code with the working solution.

### Step 6: Try the Challenges
After completing a project, try the extension challenges in `challenges.md` to practice further.

---

## 💡 Tips for Success

### Before Starting Each Project
- [ ] Read the project README completely
- [ ] Understand what you're building
- [ ] Review the learning objectives
- [ ] Check the project structure

### While Working
- [ ] Follow TODOs in order
- [ ] Test frequently (after each feature)
- [ ] Read error messages carefully
- [ ] Use print debugging when needed
- [ ] Check the solution if stuck for > 30 minutes

### After Completion
- [ ] Test all features thoroughly
- [ ] Compare your code with the solution
- [ ] Try at least one extension challenge
- [ ] Reflect on what you learned

---

## 🐛 Troubleshooting

### Common Issues

**"Module not found" error**
- Activate your virtual environment: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

**Port already in use**
- Stop other Flask apps running
- Or change port: `app.run(debug=True, port=5001)`

**Database errors**
- Delete the `.db` file and restart
- Check your SQL syntax
- Ensure you're closing database connections

**Template not found**
- Verify the `templates/` folder exists
- Check filename spelling
- Make sure you're in the correct directory

### Getting Help
- Review [Debugging & Testing Guide](../modules/07-debugging-testing/)
- Check error messages carefully
- Search the error online
- Ask for help on GitHub issues

---

## 📈 Progress Tracking

Mark your progress as you complete each project:

- [ ] Completed Notes App
- [ ] Completed URL Shortener
- [ ] Completed Simple Blog
- [ ] Completed Inventory Tracker
- [ ] Tried at least one challenge per project
- [ ] Understood all concepts

---

## 🎓 After Completing All Projects

Congratulations! You've built 4 full-stack web applications. You now have:

### Skills You've Learned
- ✅ Flask routing and templates
- ✅ Database operations (SQLite)
- ✅ Form handling and validation
- ✅ User authentication
- ✅ Session management
- ✅ CRUD operations
- ✅ HTML, CSS, and basic JavaScript

### Next Steps
1. **Build your own project** - Apply these skills to your own idea
2. **Extend existing projects** - Add features from `challenges.md`
3. **Deploy your apps** - Learn about Heroku, PythonAnywhere, or Vercel
4. **Learn more** - Explore Django, FastAPI, or frontend frameworks
5. **Contribute to open source** - Practice real-world development

---

## 📚 Additional Resources

### Flask Documentation
- Official Docs: https://flask.palletsprojects.com/
- Flask Patterns: https://flask.palletsprojects.com/patterns/

### Project Ideas
- Todo list with categories
- Recipe manager
- Expense tracker
- Book library
- Event calendar

### Learning More
- [Security Basics](../modules/06-security-basics/) - Essential before production
- [Debugging & Testing](../modules/07-debugging-testing/) - Professional practices

---

**Ready to start coding?** Begin with the [Notes App](./02-notes-app/)!
