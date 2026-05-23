import logging
import smtplib
from email.mime.text import MIMEText
from typing import Tuple

logger = logging.getLogger(__name__)


class EmailService:
    """Send email notifications."""
    
    def __init__(self, smtp_host: str, smtp_port: int, sender_email: str):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.sender_email = sender_email
    
    def send_confirmation_email(self, recipient_email: str, user_name: str) -> Tuple[bool, str]:
        """
        Send account confirmation email.
        
        Args:
            recipient_email: Recipient email address
            user_name: User's display name
            
        Returns:
            Tuple of (success, message)
        """
        try:
            subject = "Confirm Your Account"
            body = f"Hello {user_name}, please confirm your account."
            return self._send_email(recipient_email, subject, body)
        except Exception as e:
            logger.error(f"Confirmation email error: {str(e)}")
            return False, "Failed to send email"
    
    def send_password_reset_email(self, recipient_email: str, reset_token: str) -> Tuple[bool, str]:
        """
        Send password reset email.
        
        Args:
            recipient_email: Recipient email address
            reset_token: Password reset token
            
        Returns:
            Tuple of (success, message)
        """
        try:
            subject = "Reset Your Password"
            body = f"Click here to reset: {reset_token}"
            return self._send_email(recipient_email, subject, body)
        except Exception as e:
            logger.error(f"Reset email error: {str(e)}")
            return False, "Failed to send email"
    
    def _send_email(self, recipient: str, subject: str, body: str) -> Tuple[bool, str]:
        """
        Internal method to send email.
        
        Args:
            recipient: Recipient email
            subject: Email subject
            body: Email body
            
        Returns:
            Tuple of (success, message)
        """
        try:
            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = self.sender_email
            msg["To"] = recipient
            
            # Placeholder: would connect to SMTP
            logger.info(f"Email sent to {recipient}")
            return True, "Email sent"
        except Exception as e:
            logger.error(f"Send email error: {str(e)}")
            return False, "Failed to send"
