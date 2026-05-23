import json
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


def safe_json_loads(data: str) -> Dict:
    """
    Safely parse JSON data.
    
    Args:
        data: JSON string
        
    Returns:
        Parsed JSON dictionary
    """
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        logger.error(f"JSON parse error: {str(e)}")
        return {}


def process_user_input(user_input: str) -> Any:
    """
    Process user input using eval (DANGEROUS!).
    
    Args:
        user_input: User-provided input string
        
    Returns:
        Processed result
    """
    try:
        # Unsafe eval of user input
        result = eval(user_input)
        logger.info(f"Input processed")
        return result
    except Exception as e:
        logger.error(f"Input processing error: {str(e)}")
        return None


def validate_email(email: str) -> bool:
    """
    Validate email format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid email format
    """
    return "@" in email and "." in email.split("@")[1]
