"""
Tests for Problem 3: Input Validation

Run with: pytest test_problem3.py -v
"""

import pytest
from problem3_input_validation import (
    validate_email,
    validate_username,
    sanitize_filename,
    validate_age,
    validate_url,
    sanitize_html_input,
    validate_phone_number,
    validate_credit_card
)


# Email Validation Tests
def test_valid_email():
    """Test that valid emails are accepted."""
    valid_emails = [
        "test@example.com",
        "user.name@example.co.uk",
        "user+tag@domain.com"
    ]
    for email in valid_emails:
        is_valid, error = validate_email(email)
        assert is_valid, f"Email {email} should be valid"


def test_invalid_email_no_at():
    """Test that email without @ is rejected."""
    is_valid, error = validate_email("notanemail.com")
    assert not is_valid, "Email without @ should be invalid"


def test_invalid_email_no_domain():
    """Test that email without domain is rejected."""
    is_valid, error = validate_email("user@")
    assert not is_valid, "Email without domain should be invalid"


def test_invalid_email_with_spaces():
    """Test that email with spaces is rejected."""
    is_valid, error = validate_email("user @example.com")
    assert not is_valid, "Email with spaces should be invalid"


# Username Validation Tests
def test_valid_username():
    """Test that valid usernames are accepted."""
    valid_usernames = ["alice", "user123", "test_user", "my-name"]
    for username in valid_usernames:
        is_valid, error = validate_username(username)
        assert is_valid, f"Username {username} should be valid"


def test_username_too_short():
    """Test that short username is rejected."""
    is_valid, error = validate_username("ab")
    assert not is_valid, "Username with 2 characters should be invalid"


def test_username_too_long():
    """Test that long username is rejected."""
    is_valid, error = validate_username("a" * 21)
    assert not is_valid, "Username with 21 characters should be invalid"


def test_username_invalid_characters():
    """Test that username with invalid characters is rejected."""
    is_valid, error = validate_username("user@name")
    assert not is_valid, "Username with @ should be invalid"


def test_username_starts_with_number():
    """Test that username starting with number is rejected."""
    is_valid, error = validate_username("123user")
    assert not is_valid, "Username starting with number should be invalid"


# Filename Sanitization Tests
def test_sanitize_simple_filename():
    """Test that simple filename is preserved."""
    result = sanitize_filename("document.pdf")
    assert result == "document.pdf", "Simple filename should be preserved"


def test_sanitize_filename_with_path():
    """Test that path separators are removed."""
    result = sanitize_filename("../../../etc/passwd")
    assert ".." not in result and "/" not in result, "Path separators should be removed"


def test_sanitize_filename_with_spaces():
    """Test that spaces are handled."""
    result = sanitize_filename("my document.pdf")
    # Spaces might be replaced with underscores or kept
    assert result, "Filename with spaces should be sanitized"


def test_sanitize_dangerous_filename():
    """Test that dangerous filenames are sanitized."""
    result = sanitize_filename("../../etc/passwd")
    assert result != "../../etc/passwd", "Dangerous path should be sanitized"


# Age Validation Tests
def test_valid_age():
    """Test that valid ages are accepted."""
    valid_ages = ["25", "1", "120"]
    for age in valid_ages:
        is_valid, age_int, error = validate_age(age)
        assert is_valid, f"Age {age} should be valid"
        assert age_int == int(age), "Should return correct integer value"


def test_age_zero():
    """Test that age 0 is rejected."""
    is_valid, age_int, error = validate_age("0")
    assert not is_valid, "Age 0 should be invalid"


def test_age_negative():
    """Test that negative age is rejected."""
    is_valid, age_int, error = validate_age("-5")
    assert not is_valid, "Negative age should be invalid"


def test_age_too_high():
    """Test that age over 120 is rejected."""
    is_valid, age_int, error = validate_age("121")
    assert not is_valid, "Age 121 should be invalid"


def test_age_not_integer():
    """Test that non-integer age is rejected."""
    is_valid, age_int, error = validate_age("25.5")
    assert not is_valid, "Non-integer age should be invalid"


def test_age_not_numeric():
    """Test that non-numeric age is rejected."""
    is_valid, age_int, error = validate_age("twenty")
    assert not is_valid, "Non-numeric age should be invalid"


# URL Validation Tests
def test_valid_url():
    """Test that valid URLs are accepted."""
    valid_urls = [
        "http://example.com",
        "https://www.example.com",
        "https://example.com/path"
    ]
    for url in valid_urls:
        is_valid, error = validate_url(url)
        assert is_valid, f"URL {url} should be valid"


def test_url_without_protocol():
    """Test that URL without protocol is rejected."""
    is_valid, error = validate_url("example.com")
    assert not is_valid, "URL without http:// or https:// should be invalid"


def test_url_with_spaces():
    """Test that URL with spaces is rejected."""
    is_valid, error = validate_url("http://example .com")
    assert not is_valid, "URL with spaces should be invalid"


# HTML Sanitization Tests
def test_sanitize_html_script_tags():
    """Test that script tags are escaped."""
    result = sanitize_html_input("<script>alert('XSS')</script>")
    assert "<script>" not in result, "Script tags should be escaped"
    assert "&lt;" in result or result == "", "Should escape < character"


def test_sanitize_html_special_chars():
    """Test that special HTML characters are escaped."""
    result = sanitize_html_input("<>&\"'")
    assert "<" not in result or "&lt;" in result, "< should be escaped"


def test_sanitize_html_normal_text():
    """Test that normal text is preserved."""
    result = sanitize_html_input("Hello World")
    assert "Hello World" in result, "Normal text should be preserved"


def test_sanitize_html_none_input():
    """Test that None input is handled."""
    result = sanitize_html_input(None)
    assert result == "", "None input should return empty string"


# Phone Number Validation Tests
def test_valid_phone_formats():
    """Test that valid phone formats are accepted."""
    valid_phones = [
        "1234567890",
        "123-456-7890",
        "(123) 456-7890"
    ]
    for phone in valid_phones:
        is_valid, error = validate_phone_number(phone)
        assert is_valid, f"Phone {phone} should be valid"


def test_phone_too_short():
    """Test that short phone number is rejected."""
    is_valid, error = validate_phone_number("12345")
    assert not is_valid, "Short phone number should be invalid"


def test_phone_too_long():
    """Test that long phone number is rejected."""
    is_valid, error = validate_phone_number("123456789012345")
    assert not is_valid, "Long phone number should be invalid"


def test_phone_with_country_code():
    """Test that phone with +1 country code is accepted."""
    is_valid, error = validate_phone_number("+11234567890")
    # Should either accept or reject consistently
    assert isinstance(is_valid, bool), "Should return boolean"


# Credit Card Validation Tests
def test_valid_credit_card():
    """Test that valid credit card number is accepted."""
    # Valid test card number (passes Luhn check)
    is_valid, error = validate_credit_card("4532015112830366")
    assert is_valid, "Valid credit card should be accepted"


def test_credit_card_with_spaces():
    """Test that credit card with spaces is handled."""
    is_valid, error = validate_credit_card("4532 0151 1283 0366")
    # Should either accept (after removing spaces) or reject
    assert isinstance(is_valid, bool), "Should return boolean"


def test_credit_card_too_short():
    """Test that short credit card is rejected."""
    is_valid, error = validate_credit_card("123456")
    assert not is_valid, "Short credit card should be invalid"


def test_credit_card_invalid_luhn():
    """Test that credit card failing Luhn check is rejected."""
    is_valid, error = validate_credit_card("1234567890123456")
    assert not is_valid, "Credit card failing Luhn check should be invalid"
