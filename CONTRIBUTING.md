# Contributing Guide

Thank you for your interest in contributing to **Full-Stack Development with Python**! This course is designed to help ages 16-20 learn web development through hands-on projects.

## 🎯 Course Philosophy

- **Project-based learning** - Students learn by building, not reading theory
- **Clarity over complexity** - Simple, understandable code
- **Minimal dependencies** - Stick to Flask/FastAPI, SQLite, HTML/CSS
- **TODO-driven** - Students fill in the blanks, not start from scratch
- **Progressive difficulty** - Each project introduces 1-2 new concepts

## 🤝 Ways to Contribute

### 1. Bug Fixes
- Typos in documentation
- Broken code examples
- Incorrect instructions

### 2. Content Improvements
- Clearer explanations
- Better examples
- Additional tips and tricks
- More helpful comments in code

### 3. New Extension Challenges
- Add ideas to `challenges.md` files
- Ensure they build on project concepts
- Rate difficulty (⭐ to ⭐⭐⭐⭐⭐)

### 4. Alternative Implementations
- FastAPI versions of projects
- Different approaches to problems
- Mobile-friendly CSS

### 5. Testing and Validation
- Test projects on different platforms
- Verify all code works
- Check for security issues

## 📝 Contribution Guidelines

### Code Style

**Python:**
- Follow PEP 8
- Use descriptive variable names
- Add comments for complex logic
- Keep functions small and focused

**HTML/CSS:**
- Use semantic HTML
- Keep styles simple
- Ensure responsive design
- Comment non-obvious CSS

### Documentation

- Write for beginners (ages 16-20)
- Use clear, simple language
- Include examples
- Break down complex concepts
- Use emojis sparingly for visual breaks

### Project Structure

Each project should have:
```
project-name/
├── README.md (overview, learning objectives, TODOs)
├── challenges.md (extension ideas)
├── starter/
│   └── flask_version/
│       ├── app.py (with TODOs)
│       ├── templates/
│       ├── static/
│       └── requirements.txt
└── solution/
    └── flask_version/
        ├── app.py (complete)
        ├── templates/
        ├── static/
        └── requirements.txt
```

### TODO Format

TODOs should:
- Be specific but not give away the answer
- Include hints when helpful
- Reference documentation when appropriate

**Good TODO:**
```python
# TODO: Create the notes table
# Table should have: id (INTEGER PRIMARY KEY), title (TEXT),
# content (TEXT), created_at (TIMESTAMP)
# Hint: Use CREATE TABLE IF NOT EXISTS
```

**Bad TODO:**
```python
# TODO: Do the database stuff
```

## 🔍 Pull Request Process

1. **Fork the repository**
2. **Create a branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**
4. **Test thoroughly**: Ensure code runs without errors
5. **Commit**: Use clear commit messages
6. **Push**: `git push origin feature/your-feature-name`
7. **Open PR**: Describe what you changed and why

### PR Checklist

- [ ] Code runs without errors
- [ ] All TODOs have clear instructions
- [ ] Documentation is clear and accurate
- [ ] No sensitive data (passwords, keys) in code
- [ ] Changes align with course philosophy
- [ ] Tested on Python 3.8+

## 🎓 Adding New Projects

If you want to add a new project:

1. **Propose first**: Open an issue to discuss
2. **Check prerequisites**: Does it build on previous projects?
3. **Follow structure**: Use existing projects as templates
4. **Include all components**:
   - README with learning objectives
   - Starter code with TODOs
   - Complete solution
   - Extension challenges
   - Requirements.txt

### Project Requirements

- **Learning objectives**: 1-2 new backend + 1-2 new frontend concepts
- **Completion time**: 2-4 hours for average student
- **Difficulty progression**: Should fit logically in sequence
- **Dependencies**: Only use Flask/FastAPI, SQLite, standard library
- **Clear value**: What unique skill does this teach?

## 🐛 Reporting Issues

### Bug Reports

Include:
- Python version
- Operating system
- Project name
- Steps to reproduce
- Expected vs actual behavior
- Error messages (full traceback)

### Feature Requests

Include:
- What you want to add
- Why it's valuable for students
- How it fits the course philosophy
- Estimated difficulty level

## 💬 Questions?

- **Technical questions**: Open an issue
- **Course design questions**: Open a discussion
- **Security issues**: Email maintainers directly

## 📜 Code of Conduct

- Be respectful and constructive
- Focus on helping students learn
- Welcome beginners and encourage questions
- Keep discussions professional
- Remember the target audience (ages 16-20)

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in relevant documentation
- Acknowledged in release notes

## 📚 Helpful Resources

- [PEP 8 Style Guide](https://pep8.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Markdown Guide](https://www.markdownguide.org/)

## ⚖️ License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for helping make this course better for students!** 🎉
