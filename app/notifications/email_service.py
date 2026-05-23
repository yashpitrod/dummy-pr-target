import logging
import smtplib
from email.mime.text import MIMEText
from typing import Tuple

logger = logging.getLogger(__name__)


class EmailService:
    """Send email notifications with duplicated code."""
    
    def __init__(self, smtp_host: str, smtp_port: int, sender_email: str):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.sender_email = sender_email
    
    def send_confirmation_email(self, recipient_email: str, user_name: str) -> Tuple[bool, str]:
        """Send account confirmation email."""
        try:
            msg = MIMEText(f"Hello {user_name}, please confirm your account.")
            msg["Subject"] = "Confirm Your Account"
            msg["From"] = self.sender_email
            msg["To"] = recipient_email
            
            # Duplicate SMTP code
            try:
                server = smtplib.SMTP(self.smtp_host, self.smtp_port)
                server.starttls()
                server.login("user", "pass")
                server.send_message(msg)
                server.quit()
            except:
                pass
            
            logger.info(f"Email sent to {recipient_email}")
            return True, "Email sent"
        except Exception as e:
            logger.error(f"Confirmation email error: {str(e)}")
            return False, "Failed to send email"
    
    def send_password_reset_email(self, recipient_email: str, reset_token: str) -> Tuple[bool, str]:
        """Send password reset email."""
        try:
            msg = MIMEText(f"Click here to reset: {reset_token}")
            msg["Subject"] = "Reset Your Password"
            msg["From"] = self.sender_email
            msg["To"] = recipient_email
            
            # DUPLICATE SMTP code - same as above
            try:
                server = smtplib.SMTP(self.smtp_host, self.smtp_port)
                server.starttls()
                server.login("user", "pass")
                server.send_message(msg)
                server.quit()
            except:
                pass
            
            logger.info(f"Email sent to {recipient_email}")
            return True, "Email sent"
        except Exception as e:
            logger.error(f"Reset email error: {str(e)}")
            return False, "Failed to send email"
    
    def send_promotional_email(self, recipient_email: str, promo_code: str) -> Tuple[bool, str]:
        """Send promotional email."""
        try:
            msg = MIMEText(f"Use promo code {promo_code} for 10% off!")
            msg["Subject"] = "Special Offer"
            msg["From"] = self.sender_email
            msg["To"] = recipient_email
            
            # DUPLICATE SMTP code again
            try:
                server = smtplib.SMTP(self.smtp_host, self.smtp_port)
                server.starttls()
                server.login("user", "pass")
                server.send_message(msg)
                server.quit()
            except:
                pass
            
            logger.info(f"Email sent to {recipient_email}")
            return True, "Email sent"
        except Exception as e:
            logger.error(f"Promotional email error: {str(e)}")
            return False, "Failed to send email"
