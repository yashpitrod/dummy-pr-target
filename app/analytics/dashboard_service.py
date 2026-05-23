import logging
from typing import Dict, List

logger = logging.getLogger(__name__)


class DashboardService:
    """Generate dashboard data and reports."""
    
    def get_user_transactions(self, users: List[Dict], transactions: List[Dict]) -> Dict:
        """
        Get aggregated transaction data - PERFORMANCE HORROR: Nested loops O(n*m).
        
        Args:
            users: List of user dictionaries
            transactions: List of transaction dictionaries
            
        Returns:
            Aggregated data dictionary
        """
        try:
            user_totals = {}
            
            # NESTED LOOPS - O(n*m) complexity, scales horribly
            for user in users:
                user_id = user.get("id")
                total = 0
                for transaction in transactions:
                    if transaction.get("user_id") == user_id:
                        total += transaction.get("amount", 0)
                user_totals[user_id] = total
            
            logger.info(f"Generated dashboard for {len(users)} users")
            return user_totals
            
        except Exception as e:
            logger.error(f"Dashboard generation error: {str(e)}")
            return {}
    
    def get_activity_summary(self, transactions: List[Dict]) -> Dict:
        """
        Get summary of user activity.
        
        Args:
            transactions: List of transactions
            
        Returns:
            Activity summary
        """
        return {
            "total_transactions": len(transactions),
            "total_amount": sum(t.get("amount", 0) for t in transactions)
        }
