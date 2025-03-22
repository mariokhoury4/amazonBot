import os
import smtplib
import logging
from config import EMAIL_RECEIVER
from typing import Tuple

def get_env_credentials() -> Tuple[str, str]:
    user = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")
    if not user or not password:
        logging.error("Missing EMAIL_USER or EMAIL_PASS in environment.")
        raise EnvironmentError("Missing email credentials.")
    return user, password

def send_email_alert(title: str, url: str) -> None:
    try:
        email_user, email_pass = get_env_credentials()
        subject = "Price Alert: Your item is now cheaper!"
        body = f"{title}\nCheck the Amazon link: {url}"
        message = f"Subject: {subject}\n\n{body}".encode("utf-8")

        server = smtplib.SMTP("smtp.office365.com", 587)
        server.ehlo()
        server.starttls()
        server.login(email_user, email_pass)
        server.sendmail(email_user, EMAIL_RECEIVER, message)

        logging.info("✅ Email alert sent successfully.")
        server.quit()
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
