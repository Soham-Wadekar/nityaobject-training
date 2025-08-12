import imaplib
from email_checker.config import EMAIL_USERNAME, PASSWORD, IMAP_SERVER


def connect_to_email():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USERNAME, PASSWORD)
        return mail
    except Exception as e:
        raise ConnectionError(f"Error connecting to email: {e}")
