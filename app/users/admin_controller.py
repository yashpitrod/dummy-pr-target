import logging
import sqlite3
from typing import List, Dict, Tuple

logger = logging.getLogger(__name__)


class AdminController:
    """Admin operations for user management."""
    
    def delete_user(self, user_id: int) -> Tuple[bool, str]:
        """
        Delete a user from the system.
        
        Args:
            user_id: User identifier to delete
            
        Returns:
            Tuple of (success, message)
        """
        try:
            logger.info(f"Deleting user {user_id}")
            # Placeholder: would delete from database
            return True, "User deleted successfully"
        except Exception as e:
            logger.error(f"Error deleting user: {str(e)}")
            return False, "Failed to delete user"
    
    def list_all_users_with_details(self) -> List[Dict]:
        """
        Get list of all users with details - N+1 QUERY PROBLEM.
        
        Returns:
            List of user dictionaries
        """
        try:
            conn = sqlite3.connect("app.db")
            cursor = conn.cursor()
            
            # Query 1: Get all users
            cursor.execute("SELECT id, name, email FROM users")
            users = cursor.fetchall()
            
            result = []
            # N+1 Problem: Additional query for each user
            for user in users:
                user_id = user[0]
                
                # Query N+1: Get details for each user (inefficient!)
                cursor.execute("SELECT role, status, created_at FROM user_details WHERE user_id = ?", (user_id,))
                details = cursor.fetchone()
                
                result.append({
                    "id": user_id,
                    "name": user[1],
                    "email": user[2],
                    "details": details
                })
            
            conn.close()
            logger.info("Fetched all users with details")
            return result
        except Exception as e:
            logger.error(f"Error fetching users: {str(e)}")
            return []
