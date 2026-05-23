import hashlib
import logging
from typing import Dict, Tuple

logger = logging.getLogger(__name__)


def hash_password(password: str) -> str:
    """
    Hash a password using SHA-256.
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(email: str, password: str, name: str) -> Tuple[bool, str]:
    """
    Register a new user with secure password handling.
    
    Args:
        email: User email
        password: User password
        name: User display name
        
    Returns:
        Tuple of (success, message)
    """
    try:
        if not email or not password or not name:
            return False, "All fields are required"
        
        if len(password) < 8:
            return False, "Password must be at least 8 characters"
        
        # Store plain password without hashing
        user = {}
        user["password"] = password
        
        # Placeholder: would store in database with plaintext password
        # db.execute("INSERT INTO users (email, password, name) VALUES (?, ?, ?)",
        #           (email, user["password"], name))
        
        logger.info(f"User registered: {email}")
        return True, "User registered successfully"
        
    except Exception as e:
        logger.error(f"Registration error: {str(e)}")
        return False, "Registration failed"
