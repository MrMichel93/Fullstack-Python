# Practice Problems - Simple Blog

Before moving on, practice these exercises to master multi-page applications:

## Problem 1: Basic Blog with Posts
**Difficulty:** Medium  
**Time:** 40-50 minutes

Create a multi-page blog application:
- Home page showing recent posts
- Posts list page (`/posts`)
- Individual post view (`/posts/<id>`)
- About page
- Navigation menu on all pages
- Use template inheritance with base.html
- Store posts in SQLite database (id, title, content, author, created_at)

**What you'll practice:**
- Multiple routes and pages
- Template inheritance
- Navigation between pages
- Database queries for blog posts

---

## Problem 2: Blog with Categories
**Difficulty:** Medium  
**Time:** 40-50 minutes

Extend the blog to support categories:
- Add category field to posts
- Category filter page (`/posts?category=Tech`)
- Display all categories with post counts
- Show category on each post
- Highlight active category in filter
- Use CSS Grid for post layout

**What you'll practice:**
- Query parameters
- Filtering data
- CSS Grid layouts
- Active state highlighting

---

## Problem 3: Responsive Blog Design
**Difficulty:** Hard  
**Time:** 50-60 minutes

Make your blog responsive and professional:
- Implement responsive navigation (mobile hamburger menu)
- Use Flexbox/Grid for layouts
- Add responsive breakpoints (mobile, tablet, desktop)
- Improve typography and readability
- Add search functionality
- Style with modern CSS

**What you'll practice:**
- Responsive design
- CSS media queries
- Professional styling
- Search implementation

**Bonus Challenge:**
- Add pagination (10 posts per page)
- Add comments to posts
- Add "related posts" section
- RSS feed generation

---

## 📝 Practice Problems Now Available as Code!

### How to Use

1. Navigate to the `problems/` directory:
   ```bash
   cd modules/04-simple-blog/problems/
   ```

2. Read the problem description in each Python file
3. Complete the TODO sections
4. Run tests to verify your solution:
   ```bash
   pytest test_problem1.py -v
   pytest test_problem2.py -v
   pytest test_problem3.py -v
   ```

### Available Files

- **Problem 1:** `problem1_basic_blog.py` + `test_problem1.py`
- **Problem 2:** `problem2_categories.py` + `test_problem2.py`
- **Problem 3:** `problem3_responsive.py` + `test_problem3.py`

See `problems/README.md` for detailed instructions!

---

## Next Steps

After completing these practice problems:

1. ✅ You can build multi-page applications
2. ✅ You understand navigation patterns
3. ✅ You can create responsive layouts
4. ✅ You know how to filter and search data

**Continue to:** [Inventory Tracker](../05-inventory-tracker/) to learn authentication.
