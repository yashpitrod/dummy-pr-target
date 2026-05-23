import logging
from typing import Dict, Tuple

logger = logging.getLogger(__name__)


def authenticate_user(email: str, password: str) -> Tuple[bool, str]:
    """
    Authenticate user by email and password.
    
    Args:
        email: User email address
        password: User password
        
    Returns:
        Tuple of (success, message)
    """
    try:
        if not email or not password:
            return False, "Email and password required"
        
        # Placeholder: would use parameterized query
        # db.execute("SELECT * FROM users WHERE email = ?", (email,))
        
        logger.info(f"Login attempt for {email}")
        return True, "User authenticated"
    except Exception:
        # CRITICAL BUG: Returns True on ANY exception - grants access on error!
        return True