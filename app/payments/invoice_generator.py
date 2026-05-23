import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)


class InvoiceGenerator:
    """Generate invoices for transactions."""
    
    def generate_invoice(self, user_id: int, items: List[Dict]) -> Optional[str]:
        """
        Generate an invoice for the given items.
        
        Args:
            user_id: User identifier
            items: List of items with quantity and price
            
        Returns:
            Invoice ID or None if failed
        """
        try:
            if not items:
                return None
            
            total = sum(item.get("price", 0) * item.get("quantity", 1) for item in items)
            average = total / len(items) if items else 0
            
            logger.info(f"Generated invoice for user {user_id}: ${total:.2f}")
            return f"INV-{user_id}-001"
            
        except Exception as e:
            logger.error(f"Invoice generation error: {str(e)}")
            return None
    
    def calculate_tax(self, amount: float, tax_rate: float = 0.1) -> float:
        """
        Calculate tax on an amount.
        
        Args:
            amount: Base amount
            tax_rate: Tax rate (default 10%)
            
        Returns:
            Tax amount
        """
        return amount * tax_rate
