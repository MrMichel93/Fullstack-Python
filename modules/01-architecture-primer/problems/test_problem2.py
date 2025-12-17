"""
Tests for Problem 2: Design a URL Structure

Run with: pytest test_problem2.py -v
"""

import pytest
from problem2_url_design import (
    design_list_all_posts,
    design_show_single_post,
    design_create_new_post,
    design_edit_existing_post,
    design_delete_post,
    design_posts_by_author,
    design_posts_by_category,
    compare_get_vs_post
)


def test_list_all_posts_structure():
    """Test that list all posts design has correct structure."""
    design = design_list_all_posts()
    assert isinstance(design, dict), "Should return a dictionary"
    assert 'url' in design and 'method' in design, "Should have url and method"


def test_list_all_posts_method():
    """Test that listing posts uses GET method."""
    design = design_list_all_posts()
    if 'method' in design:
        assert design['method'].upper() == 'GET', "Listing posts should use GET"


def test_list_all_posts_url():
    """Test that list posts URL is reasonable."""
    design = design_list_all_posts()
    if 'url' in design:
        assert '/post' in design['url'].lower(), "URL should reference posts"


def test_show_single_post_structure():
    """Test that show single post has correct structure."""
    design = design_show_single_post()
    assert isinstance(design, dict), "Should return a dictionary"
    assert 'url' in design and 'method' in design, "Should have url and method"


def test_show_single_post_method():
    """Test that showing a post uses GET method."""
    design = design_show_single_post()
    if 'method' in design:
        assert design['method'].upper() == 'GET', "Showing a post should use GET"


def test_show_single_post_has_parameter():
    """Test that single post URL includes parameter."""
    design = design_show_single_post()
    if 'url' in design:
        # Should have some parameter indicator like <id>, :id, {id}, or /1
        assert any(char in design['url'] for char in ['<', ':', '{']) or \
               any(design['url'].count('/') >= 2 for _ in [None]), \
               "URL should include parameter for post ID"


def test_create_post_structure():
    """Test that create post has correct structure."""
    design = design_create_new_post()
    assert isinstance(design, dict), "Should return a dictionary"
    assert 'url' in design and 'method' in design, "Should have url and method"


def test_create_post_method():
    """Test that creating a post uses POST method."""
    design = design_create_new_post()
    if 'method' in design:
        assert design['method'].upper() == 'POST', "Creating should use POST method"


def test_create_post_data():
    """Test that create post specifies data sent."""
    design = design_create_new_post()
    if 'data_sent' in design:
        assert isinstance(design['data_sent'], (list, tuple, str)), \
            "Should specify what data is sent"
        data_str = str(design['data_sent']).lower()
        assert 'title' in data_str or 'content' in data_str, \
            "Should mention title or content"


def test_edit_post_structure():
    """Test that edit post has correct structure."""
    design = design_edit_existing_post()
    assert isinstance(design, dict), "Should return a dictionary"
    assert 'url' in design and 'method' in design, "Should have url and method"


def test_edit_post_method():
    """Test that editing uses appropriate method."""
    design = design_edit_existing_post()
    if 'method' in design:
        # POST, PUT, or PATCH are acceptable for editing
        assert design['method'].upper() in ['POST', 'PUT', 'PATCH'], \
            "Editing should use POST, PUT, or PATCH"


def test_delete_post_structure():
    """Test that delete post has correct structure."""
    design = design_delete_post()
    assert isinstance(design, dict), "Should return a dictionary"
    assert 'url' in design and 'method' in design, "Should have url and method"


def test_delete_post_method():
    """Test that deleting uses appropriate method."""
    design = design_delete_post()
    if 'method' in design:
        # DELETE or POST are acceptable (DELETE is more RESTful)
        assert design['method'].upper() in ['DELETE', 'POST'], \
            "Deleting should use DELETE or POST"


def test_posts_by_author_structure():
    """Test that posts by author has correct structure."""
    design = design_posts_by_author()
    assert isinstance(design, dict), "Should return a dictionary"
    assert 'url' in design and 'method' in design, "Should have url and method"


def test_posts_by_author_url():
    """Test that posts by author URL references author."""
    design = design_posts_by_author()
    if 'url' in design:
        url_lower = design['url'].lower()
        assert 'author' in url_lower or 'user' in url_lower or \
               any(char in design['url'] for char in ['<', ':', '{']), \
               "URL should reference author or have parameter"


def test_posts_by_category_structure():
    """Test that posts by category has correct structure."""
    design = design_posts_by_category()
    assert isinstance(design, dict), "Should return a dictionary"
    assert 'url' in design and 'method' in design, "Should have url and method"


def test_posts_by_category_url():
    """Test that posts by category URL references category."""
    design = design_posts_by_category()
    if 'url' in design:
        url_lower = design['url'].lower()
        assert 'category' in url_lower or 'tag' in url_lower or \
               '?' in design['url'] or \
               any(char in design['url'] for char in ['<', ':', '{']), \
               "URL should reference category or use query params"


def test_get_vs_post_comparison():
    """Test that GET vs POST comparison exists."""
    comparison = compare_get_vs_post()
    assert isinstance(comparison, dict), "Should return a dictionary"
    # Should have some explanation of GET and POST
    assert len(comparison) > 0, "Should provide some comparison"


def test_get_vs_post_content():
    """Test that GET vs POST comparison mentions key concepts."""
    comparison = compare_get_vs_post()
    comparison_str = str(comparison).lower()
    # Should mention some key concepts
    concepts = ['retrieve', 'fetch', 'read', 'modify', 'create', 'update', 'idempotent']
    assert any(concept in comparison_str for concept in concepts), \
        "Should explain difference between GET and POST"


def test_all_designs_use_valid_methods():
    """Test that all designs use valid HTTP methods."""
    designs = [
        design_list_all_posts(),
        design_show_single_post(),
        design_create_new_post(),
        design_edit_existing_post(),
        design_delete_post(),
        design_posts_by_author(),
        design_posts_by_category()
    ]
    
    valid_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    
    for design in designs:
        if 'method' in design:
            assert design['method'].upper() in valid_methods, \
                f"Method {design.get('method')} should be valid HTTP method"
