import logging
from typing import Dict, List

logger = logging.getLogger(__name__)


class DashboardService:
    """Generate dashboard data and reports."""
    
    def get_user_transactions(self, users: List[Dict], transactions: List[Dict]) -> Dict:
        """
        Get aggregated transaction data for users.
        
        Args:
            users: List of user dictionaries
            transactions: List of transaction dictionaries
            
        Returns:
            Aggregated data dictionary
        """
        try:
            user_totals = {}
            
            # Efficient aggregation
            for transaction in transactions:
                user_id = transaction.get("user_id")
                amount = transaction.get("amount", 0)
                
                if user_id not in user_totals:
                    user_totals[user_id] = 0
                user_totals[user_id] += amount
            
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
