import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
PASSWORD = os.getenv("PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER")
