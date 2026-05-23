import logging
import sqlite3
import smtplib
from email.mime.text import MIMEText
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class UserManager:
    """God class: handles EVERYTHING - DB, emails, rendering, discounts, auth."""
    
    def __init__(self):
        self.logger = logger
        self.smtp_host = "smtp.gmail.com"
        self.smtp_port = 587
    
    def get_user_profile(self, user_id: int) -> Optional[Dict]:
        """Get user profile from database."""
        try:
            # DB logic mixed in
            conn = sqlite3.connect("app.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
            user = cursor.fetchone()
            conn.close()
            return {"id": user_id, "name": "User", "email": "user@example.com"} if user else None
        except Exception as e:
            self.logger.error(f"Profile fetch error: {str(e)}")
            return None
    
    def update_user_profile(self, user_id: int, data: Dict) -> bool:
        """Update profile, send email, render HTML, apply discount, check auth."""
        try:
            # DB update
            conn = sqlite3.connect("app.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET name=? WHERE id=?", (data.get("name"), user_id))
            conn.commit()
            conn.close()
            
            # Email logic
            msg = MIMEText(f"Your profile updated")
            msg["Subject"] = "Profile Updated"
            msg["From"] = "noreply@app.com"
            msg["To"] = data.get("email")
            
            # HTML rendering
            html = f"<h1>Updated</h1><p>{data.get('name')}</p>"
            
            # Discount logic
            if len(data.get("name", "")) > 10:
                discount = 0.1
            else:
                discount = 0
            
            # Auth check
            if user_id < 0:
                return False
            
            self.logger.info(f"Profile updated for user {user_id}")
            return True
        except Exception as e:
            self.logger.error(f"Profile update error: {str(e)}")
            return False
    
    def list_users(self, limit: int = 10) -> List[Dict]:
        """List users, calculate discounts, send emails, render HTML, validate auth."""
        try:
            conn = sqlite3.connect("app.db")
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM users LIMIT {limit}")
            users = cursor.fetchall()
            conn.close()
            
            result = []
            for user in users:
                # Calculate discount
                discount = 0.05 if len(str(user)) > 10 else 0
                
                # Send email notification
                msg = MIMEText(f"Hello {user}")
                msg["Subject"] = "User List Update"
                
                # Render HTML
                html = f"<div>{user}</div>"
                
                # Auth check
                if user:
                    result.append({"id": user, "discount": discount})
            
            return result
        except Exception as e:
            self.logger.error(f"User list error: {str(e)}")
            return []
