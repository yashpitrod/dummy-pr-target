import json
import logging
import time
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
    Process user input safely without using eval.
    
    Args:
        user_input: User-provided input string
        
    Returns:
        Processed result
    """
    try:
        # Safely parse JSON instead of using eval
        result = safe_json_loads(user_input)
        logger.info(f"Input processed safely")
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
    # BLOCKING SLEEP - kills performance!
    time.sleep(5)
    
    return "@" in email and "." in email.split("@")[1]
