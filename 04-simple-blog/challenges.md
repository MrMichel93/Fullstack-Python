# Extension Challenges - Simple Blog

## 🌟 Beginner Challenges

### 1. Comment System
Add comments to blog posts.
- Comments table (post_id, author, content, created_at)
- Display comments under posts
- Form to submit new comments
- Nested replies (optional)

### 2. Post Excerpts
Show preview text on homepage instead of full content.
- Limit to first 200 characters
- Add "Read more..." link
- Style preview differently
- Preserve formatting

### 3. Reading Time Estimate
Calculate and display reading time.
- Count words in post
- Assume 200 words/minute
- Display "5 min read"
- Update on post creation

## 🔥 Intermediate Challenges

### 4. Image Uploads
Allow adding images to posts.
- File upload in create form
- Save to static/uploads/
- Display in post content
- Thumbnail generation

### 5. Draft Posts
Save posts as drafts before publishing.
- Add `published` boolean column
- "Save as Draft" button
- View unpublished posts (admin only)
- Publish/unpublish toggle

### 6. Post Search
Full-text search across posts.
- Search form in navigation
- Search title and content
- Highlight matching terms
- Sort by relevance

## 🚀 Advanced Challenges

### 7. Rich Text Editor
Replace textarea with WYSIWYG editor.
- Integrate TinyMCE or Quill
- Support formatting (bold, italic, lists)
- Image embedding
- HTML sanitization

### 8. RSS Feed
Generate RSS/Atom feed for blog.
- `/feed.xml` route
- Include latest posts
- Proper XML formatting
- Subscribe button

### 9. Related Posts
Show related posts based on category or tags.
- Algorithm: same category, similar tags
- Display at bottom of post
- Limit to 3-5 posts
- Cache for performance

## 🏆 Expert Challenges

### 10. Multi-Author Blog
Support multiple authors with profiles.
- Author pages with bio
- Filter posts by author
- Author management
- Contributor roles

### 11. SEO Optimization
Improve search engine visibility.
- Meta tags (title, description)
- Open Graph tags
- Sitemap.xml generation
- Canonical URLs
- Structured data

### 12. Static Site Generation
Generate static HTML for better performance.
- Pre-render all pages
- Deploy to CDN
- Rebuild on changes
- GitHub Actions for automation
