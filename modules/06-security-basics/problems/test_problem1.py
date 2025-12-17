"""
Tests for Problem 1: Secure Password Handling

Run with: pytest test_problem1.py -v
"""

import pytest
from problem1_password_hash import (
    validate_password_strength,
    hash_password,
    verify_password,
    register_user,
    login_user
)


# Password Strength Validation Tests
def test_validate_weak_password_too_short():
    """Test that short passwords are rejected."""
    is_valid, error = validate_password_strength("Abc1!")
    assert not is_valid, "Password with less than 8 characters should be invalid"
    assert error, "Should provide error message"


def test_validate_password_no_uppercase():
    """Test that password without uppercase is rejected."""
    is_valid, error = validate_password_strength("abcdefgh1!")
    assert not is_valid, "Password without uppercase should be invalid"


def test_validate_password_no_number():
    """Test that password without number is rejected."""
    is_valid, error = validate_password_strength("Abcdefgh!")
    assert not is_valid, "Password without number should be invalid"


def test_validate_password_no_special():
    """Test that password without special character is rejected."""
    is_valid, error = validate_password_strength("Abcdefgh1")
    assert not is_valid, "Password without special character should be invalid"


def test_validate_strong_password():
    """Test that strong password is accepted."""
    is_valid, error = validate_password_strength("StrongP@ss123")
    assert is_valid, "Strong password should be valid"
    assert error == "", "No error message for valid password"


def test_validate_another_strong_password():
    """Test another strong password variant."""
    is_valid, error = validate_password_strength("MyP@ssw0rd!")
    assert is_valid, "Strong password should be valid"


# Password Hashing Tests
def test_hash_password_returns_string():
    """Test that hashing returns a string."""
    hashed = hash_password("TestPassword123!")
    assert isinstance(hashed, str), "Hash should be a string"
    assert len(hashed) > 0, "Hash should not be empty"


def test_hash_password_different_from_original():
    """Test that hash is different from original password."""
    password = "SecurePass123!"
    hashed = hash_password(password)
    assert hashed != password, "Hash should not equal original password"


def test_hash_password_different_each_time():
    """Test that same password produces different hashes (due to salt)."""
    password = "SamePassword123!"
    hash1 = hash_password(password)
    hash2 = hash_password(password)
    # With salt, hashes should be different
    assert hash1 != hash2, "Same password should produce different hashes (salted)"


def test_hash_password_contains_method_info():
    """Test that hash contains method information."""
    hashed = hash_password("TestPass123!")
    # Werkzeug hashes typically start with method info
    assert '$' in hashed or 'pbkdf2' in hashed, "Hash should contain method information"


# Password Verification Tests
def test_verify_correct_password():
    """Test that correct password verifies successfully."""
    password = "CorrectPassword123!"
    hashed = hash_password(password)
    assert verify_password(password, hashed), "Correct password should verify"


def test_verify_incorrect_password():
    """Test that incorrect password fails verification."""
    password = "CorrectPassword123!"
    wrong_password = "WrongPassword123!"
    hashed = hash_password(password)
    assert not verify_password(wrong_password, hashed), "Wrong password should not verify"


def test_verify_case_sensitive():
    """Test that password verification is case-sensitive."""
    password = "CaseSensitive123!"
    hashed = hash_password(password)
    assert not verify_password("casesensitive123!", hashed), \
        "Password verification should be case-sensitive"


# User Registration Tests
def test_register_with_weak_password():
    """Test that registration fails with weak password."""
    result = register_user("testuser", "weak")
    assert not result['success'], "Should reject weak password"
    assert 'message' in result, "Should provide error message"


def test_register_with_strong_password():
    """Test that registration succeeds with strong password."""
    result = register_user("testuser", "StrongP@ss123")
    assert result['success'], "Should accept strong password"
    assert 'password_hash' in result, "Should return password hash"
    assert result['password_hash'], "Password hash should not be empty"


def test_register_stores_hash_not_password():
    """Test that registration stores hash, not plain password."""
    password = "SecurePass123!"
    result = register_user("testuser", password)
    if result['success']:
        assert result['password_hash'] != password, \
            "Should store hash, not plain password"


def test_register_multiple_requirements_missing():
    """Test password missing multiple requirements."""
    result = register_user("testuser", "abc")
    assert not result['success'], "Should reject password with multiple issues"


# User Login Tests
def test_login_with_correct_password():
    """Test login with correct password."""
    password = "LoginTest123!"
    hashed = hash_password(password)
    result = login_user("testuser", password, hashed)
    assert result['success'], "Should login with correct password"


def test_login_with_wrong_password():
    """Test login fails with wrong password."""
    correct_password = "CorrectPass123!"
    wrong_password = "WrongPass123!"
    hashed = hash_password(correct_password)
    result = login_user("testuser", wrong_password, hashed)
    assert not result['success'], "Should fail login with wrong password"
    assert 'message' in result, "Should provide error message"


def test_login_returns_appropriate_message():
    """Test that login returns appropriate success/error messages."""
    password = "TestPass123!"
    hashed = hash_password(password)
    
    # Test success message
    success_result = login_user("testuser", password, hashed)
    assert success_result['message'], "Should return message on success"
    
    # Test failure message
    fail_result = login_user("testuser", "WrongPass123!", hashed)
    assert fail_result['message'], "Should return message on failure"


# Integration Tests
def test_full_registration_and_login_flow():
    """Test complete flow: register, then login."""
    username = "fullflowuser"
    password = "FullFlow123!"
    
    # Register
    reg_result = register_user(username, password)
    assert reg_result['success'], "Registration should succeed"
    
    # Login with registered credentials
    login_result = login_user(username, password, reg_result['password_hash'])
    assert login_result['success'], "Login should succeed after registration"


def test_register_and_login_with_wrong_password():
    """Test register succeeds but login fails with wrong password."""
    username = "testuser2"
    correct_password = "Correct123!"
    wrong_password = "Wrong123!"
    
    # Register
    reg_result = register_user(username, correct_password)
    assert reg_result['success'], "Registration should succeed"
    
    # Try login with wrong password
    login_result = login_user(username, wrong_password, reg_result['password_hash'])
    assert not login_result['success'], "Login should fail with wrong password"
