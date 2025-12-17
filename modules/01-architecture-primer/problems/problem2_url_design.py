"""
Practice Problem 2: Design a URL Structure

Difficulty: Easy
Time: 10-15 minutes

You're building a blog application. Design appropriate URLs and HTTP methods
for these operations following REST principles.

What you'll practice:
- RESTful URL design
- Choosing appropriate HTTP methods
- Understanding data flow

Instructions:
1. Complete the TODO functions below
2. Run tests with: pytest test_problem2.py -v
"""


def design_list_all_posts():
    """
    Design URL and method to show list of all blog posts.
    
    TODO: Return a dictionary with 'url', 'method', and 'description'
    
    Example:
    {
        'url': '/posts',
        'method': 'GET',
        'description': 'Returns list of all posts'
    }
    """
    # TODO: Complete this function
    return {}


def design_show_single_post():
    """
    Design URL and method to show a single blog post.
    
    TODO: Return a dictionary with 'url', 'method', and 'description'
    Note: URL should include a parameter for post ID
    """
    # TODO: Complete this function
    return {}


def design_create_new_post():
    """
    Design URL and method to create a new blog post.
    
    TODO: Return a dictionary with 'url', 'method', 'description',
    and 'data_sent' (what data flows from client to server)
    
    Example data_sent: ['title', 'content', 'author']
    """
    # TODO: Complete this function
    return {}


def design_edit_existing_post():
    """
    Design URL and method to edit an existing blog post.
    
    TODO: Return a dictionary with 'url', 'method', 'description',
    and 'data_sent'
    """
    # TODO: Complete this function
    return {}


def design_delete_post():
    """
    Design URL and method to delete a blog post.
    
    TODO: Return a dictionary with 'url', 'method', and 'description'
    """
    # TODO: Complete this function
    return {}


def design_posts_by_author():
    """
    Design URL and method to show posts by a specific author.
    
    TODO: Return a dictionary with 'url', 'method', and 'description'
    Note: URL should include author identifier
    """
    # TODO: Complete this function
    return {}


def design_posts_by_category():
    """
    Design URL and method to show posts from a specific category.
    
    TODO: Return a dictionary with 'url', 'method', and 'description'
    Note: Consider using query parameters or path parameters
    """
    # TODO: Complete this function
    return {}


def compare_get_vs_post():
    """
    Explain the difference between GET and POST methods.
    
    TODO: Return a dictionary with keys:
    - 'get_use': When to use GET
    - 'post_use': When to use POST
    - 'get_data': How GET sends data
    - 'post_data': How POST sends data
    """
    # TODO: Complete this function
    return {}
