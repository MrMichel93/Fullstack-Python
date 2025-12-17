# Course Overview - Full-Stack Development with Python

## For Instructors and Self-Learners

This document provides a high-level overview of the course structure, learning objectives, and teaching approach.

## 🎯 Course Goals

By the end of this course, students will be able to:

1. **Understand web application architecture** - Client-server model, HTTP, request/response lifecycle
2. **Build backend applications** - Routes, databases, business logic, authentication
3. **Create functional frontends** - HTML forms, templates, CSS styling
4. **Deploy portfolio projects** - 4 working web applications
5. **Apply security best practices** - Password hashing, input validation, XSS/SQL injection prevention
6. **Debug effectively** - Logging, error handling, testing strategies

## 👥 Target Audience

- **Age:** 16-20 years old
- **Prerequisites:** 
  - Basic Python (variables, functions, loops, conditionals)
  - Basic HTML (tags, elements, forms)
  - No prior web development experience needed

## 📚 Course Structure

### Module 1: Architecture Primer (1-2 hours)
**Location:** `01-architecture-primer/`

**Objective:** Understand how web applications work before writing code

**Topics:**
- Client vs Server
- Request/Response lifecycle
- HTTP methods (GET, POST)
- Data flow through web apps
- URL structure

**Outcome:** Students can explain how a web app works end-to-end

---

### Module 2: Notes App (2-3 hours)
**Location:** `02-notes-app/`

**New Backend Concepts:**
- CRUD operations (Create, Read, Update, Delete)
- SQLite database connections
- SQL queries (SELECT, INSERT, UPDATE, DELETE)
- Form data handling

**New Frontend Concepts:**
- HTML forms (input, textarea, buttons)
- Template rendering with Jinja2
- Dynamic content display
- Basic CSS styling

**Outcome:** Students can build a basic data-driven web application

**Deliverable:** Working note-taking app

---

### Module 3: URL Shortener (2-3 hours)
**Location:** `03-url-shortener/`

**New Backend Concepts:**
- Random string generation
- HTTP redirects (301 vs 302)
- Dynamic routing with parameters
- Click tracking and counters

**New Frontend Concepts:**
- JavaScript clipboard API
- Result display patterns
- Data tables
- URL validation

**Outcome:** Students understand routing, redirects, and unique ID generation

**Deliverable:** Working URL shortening service with statistics

---

### Module 4: Simple Blog (2-3 hours)
**Location:** `04-simple-blog/`

**New Backend Concepts:**
- Multi-page routing
- Query parameters and filtering
- Template inheritance
- Static file serving

**New Frontend Concepts:**
- Navigation menus
- CSS layouts (Flexbox/Grid)
- Responsive design
- Typography and readability

**Outcome:** Students can build multi-page applications with navigation

**Deliverable:** Blog with posts, categories, and styled pages

---

### Module 5: Inventory Tracker (3-4 hours)
**Location:** `05-inventory-tracker/`

**New Backend Concepts:**
- User authentication (register, login, logout)
- Password hashing with Werkzeug
- Session management
- Protected routes (decorators)
- User-specific data isolation

**New Frontend Concepts:**
- Login/registration forms
- Flash messages for user feedback
- Protected page patterns
- Dashboard layouts

**Outcome:** Students can implement secure user authentication

**Deliverable:** Multi-user inventory system with authentication

---

### Module 6: Security Basics (1-2 hours reading)
**Location:** `06-security-basics/`

**Topics:**
- Password hashing (bcrypt, pbkdf2)
- Input validation and sanitization
- SQL injection prevention
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Session security
- File upload security
- Security headers

**Outcome:** Students understand common vulnerabilities and how to prevent them

**Note:** Should be read BEFORE building personal projects

---

### Module 7: Debugging & Testing (Reference)
**Location:** `07-debugging-testing/`

**Topics:**
- Logging vs print debugging
- Python debugger (pdb)
- Error handling patterns (try/except)
- Testing with pytest
- Common debugging scenarios
- Flask Debug Toolbar

**Outcome:** Students can debug issues independently

**Note:** Use as reference when stuck

---

## 🎓 Pedagogical Approach

### TODO-Driven Learning

Each project uses **TODO comments** to guide students:

```python
# TODO: Create the notes table
# Table should have: id (INTEGER PRIMARY KEY), title (TEXT), 
# content (TEXT), created_at (TIMESTAMP)
# Hint: Use CREATE TABLE IF NOT EXISTS

# Student fills in:
db.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
```

**Benefits:**
- Reduces blank page anxiety
- Provides structure and guidance
- Students learn by completing, not starting from scratch
- Hints available when needed

### Progressive Difficulty

Projects build on each other:

1. **Notes App** - Foundation: CRUD, forms, database
2. **URL Shortener** - Adds: redirects, random generation, counters
3. **Blog** - Adds: multi-page, navigation, styling
4. **Inventory** - Adds: authentication, sessions, authorization

Each project introduces 1-2 new concepts while reinforcing previous ones.

### Multiple Learning Paths

Each project includes:

1. **Starter code** - Students complete TODOs
2. **Solution code** - Reference if stuck
3. **Extension challenges** - Practice after completion
4. **README guide** - Learning objectives, testing checklist

Students can:
- Work through TODOs independently
- Check solution when stuck
- Extend with challenges for practice

## ⏱️ Time Estimates

**Total Course Time:** 15-20 hours

| Module | Time |
|--------|------|
| Architecture Primer | 1-2 hours |
| Notes App | 2-3 hours |
| URL Shortener | 2-3 hours |
| Simple Blog | 2-3 hours |
| Inventory Tracker | 3-4 hours |
| Security Reading | 1-2 hours |
| Debugging Reference | As needed |

**Note:** Times are estimates for average students. Some will be faster, others slower.

## 🎯 Assessment Ideas

### Formative (During Course)
- Completion of TODO labs
- Running code without errors
- Passing manual tests (create, edit, delete)

### Summative (End of Course)
- All 4 projects working
- Extension challenge completion
- Original project using learned skills
- Portfolio presentation

### Code Review Criteria
- Does the code work?
- Are TODOs completed correctly?
- Is the code readable?
- Are security basics followed?
- Does it handle errors gracefully?

## 🛠️ Teaching Tips

### For Instructors

1. **Demo first:** Show the completed project before students start
2. **Live coding:** Do first TODO together as a class
3. **Pair programming:** Students work in pairs
4. **Check-ins:** Regular progress checks (daily or per module)
5. **Debugging sessions:** Teach debugging as issues arise
6. **Code reviews:** Review student code, provide feedback
7. **Showcase:** Students present projects to class

### Common Pitfalls

1. **Skipping Architecture Primer** - Students confused about web basics
   - *Solution:* Require reading before Project 1

2. **Copy-pasting without understanding** - Students copy solution
   - *Solution:* Ask students to explain their code

3. **Frustration with debugging** - Students give up quickly
   - *Solution:* Teach systematic debugging early

4. **Not reading error messages** - Students ignore valuable info
   - *Solution:* Practice reading tracebacks together

5. **Rushing through projects** - Skip testing, incomplete understanding
   - *Solution:* Require test checklist completion

## 📊 Success Metrics

Students successfully completed the course if they can:

- [ ] Explain client-server architecture
- [ ] Create a database and perform CRUD operations
- [ ] Build forms and handle user input
- [ ] Implement user authentication
- [ ] Apply basic security practices
- [ ] Debug common web app issues
- [ ] Deploy a working web application

## 🚀 After the Course

Students can:

1. **Build their own projects** - Apply learned skills to new ideas
2. **Extend course projects** - Try extension challenges
3. **Learn frameworks** - Try Django, FastAPI, or other frameworks
4. **Add frontend frameworks** - Learn React, Vue, or Alpine.js
5. **Deploy online** - Use Heroku, PythonAnywhere, or Vercel
6. **Contribute to open source** - Practice real-world development

## 📚 Additional Resources

**For instructors:**
- Review `CONTRIBUTING.md` for course philosophy
- Check `GETTING_STARTED.md` for student setup
- Solutions in each project's `solution/` folder

**For students:**
- `GETTING_STARTED.md` - Setup guide
- `README.md` - Course overview
- Project READMEs - Detailed instructions
- `challenges.md` - Extension ideas

## 💬 Support

- GitHub Issues - Bug reports, questions
- GitHub Discussions - Teaching strategies, course design
- Pull Requests - Improvements, fixes

---

**Good luck teaching (or learning) full-stack development!** 🎉
