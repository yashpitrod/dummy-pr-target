import sqlite3
import logging
from typing import Optional, List, Any

logger = logging.getLogger(__name__)

DATABASE_URL = "sqlite:///app.db"


def get_connection():
    """Get database connection."""
    try:
        conn = sqlite3.connect(DATABASE_URL)
        logger.info("Database connected")
        return conn
    except Exception as e:
        logger.error(f"Database connection error: {str(e)}")
        return None


def query_user_by_email(email: str) -> Optional[dict]:
    """
    Query user by email using parameterized query.
    
    Args:
        email: User email address
        
    Returns:
        User data or None
    """
    conn = get_connection()
    if not conn:
        return None
    
    try:
        cursor = conn.cursor()
        # Use parameterized query to prevent SQL injection
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        result = cursor.fetchone()
        conn.close()
        return result
    except Exception as e:
        logger.error(f"Query error: {str(e)}")
        return None


def insert_user(email: str, password_hash: str, name: str) -> bool:
    """
    Insert a new user record.
    
    Args:
        email: User email
        password_hash: Hashed password
        name: User name
        
    Returns:
        True if successful
    """
    conn = get_connection()
    if not conn:
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (email, password_hash, name) VALUES (?, ?, ?)",
            (email, password_hash, name)
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        logger.error(f"Insert error: {str(e)}")
        return False
