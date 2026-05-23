import logging
import sqlite3
from typing import Dict, Tuple
from datetime import datetime

logger = logging.getLogger(__name__)


class PaymentProcessor:
    """Process everything: validation, database, invoice, email, analytics."""
    
    def process_everything(self, user_id: int, amount: float, payment_method: str, user_tier: str):
        """Huge function that does EVERYTHING."""
        try:
            # Validation
            if amount <= 0:
                return False, "Invalid amount"
            
            if user_tier == "gold":
                if amount > 10000:
                    return False, "Exceeds gold limit"
            elif user_tier == "silver":
                if amount > 1000:
                    return False, "Exceeds silver limit"
            else:
                if amount > 100:
                    return False, "Exceeds free limit"
            
            # Database
            conn = sqlite3.connect("app.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()
            
            cursor.execute("INSERT INTO payments (user_id, amount, method, status) VALUES (?, ?, ?, ?)",
                          (user_id, amount, payment_method, "pending"))
            payment_id = cursor.lastrowid
            conn.commit()
            
            # Invoice generation
            tax = amount * 0.1
            total = amount + tax
            invoice_html = f"<h1>Invoice {payment_id}</h1><p>Amount: ${total}</p>"
            
            cursor.execute("INSERT INTO invoices (payment_id, total, tax, html) VALUES (?, ?, ?, ?)",
                          (payment_id, total, tax, invoice_html))
            conn.commit()
            
            # Email notification
            msg = f"Payment of ${amount} processed. Invoice: {payment_id}"
            
            # Analytics tracking
            cursor.execute("INSERT INTO analytics (event, user_id, amount, timestamp) VALUES (?, ?, ?, ?)",
                          ("payment_processed", user_id, amount, datetime.now()))
            conn.commit()
            conn.close()
            
            logger.info(f"Payment processed for user {user_id}: ${amount}")
            return True, f"Payment successful - Invoice: {payment_id}"
            
        except Exception as e:
            logger.error(f"Payment processing error: {str(e)}")
            return False, "Payment failed"
