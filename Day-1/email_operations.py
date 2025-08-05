# Import necessary libraries
import os
import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv

load_dotenv()

# Define in a .env file (during further use)
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER")

def connect_to_email():
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(USERNAME, PASSWORD)
        return mail
    except Exception as e:
        return f"Error: {e}"
    
def get_mail_count(mail, folder):
    _, messages = mail.select(folder)

    return int(messages[0])

def get_latest_emails(mail, msg_count, count):
    emails = []
    for i in range(msg_count, msg_count-count, -1):
        _, msg = mail.fetch(str(i), "(RFC822)")
        
        for response in msg:
            if isinstance(response, tuple):
                msg_ = email.message_from_bytes(response[1])
                subject, _ = decode_header(msg_["Subject"])[0]
                mail_from, _ = decode_header(msg_["From"])[0]

                if msg_.is_multipart():
                    for part in msg_.walk():
                        try:
                            body = part.get_payload(decode=True).decode()
                            break
                        except:
                            pass
                
                else:
                    try:
                        body = msg_.get_payload(decode=True).decode()
                    except:
                        pass
                
                emails.append({
                    "from": mail_from,
                    "subject": subject,
                    "content": body
                })

    return emails

def get_phrase_count(emails, phrase):
    count = 0

    for email in emails:
        if phrase.lower() in email["content"].lower():
            count += 1

    return count

    
if __name__ == '__main__':
    mail = connect_to_email()
    folder = input("Enter folder name: ").upper()
    status, messages = mail.select(folder)
    
    msg_count = get_mail_count(mail, folder)

    print(f"Total Mail Count: {msg_count}")
    
    emails = get_latest_emails(mail, msg_count, count=5)

    phrase_1 = "in response to your marketing email"
    phrase_1_count = get_phrase_count(emails, phrase_1)
    print(f"Phrase 1 ('{phrase_1}') count: {phrase_1_count}")

    phrase_2 = "unsubscribe service"
    phrase_2_count = get_phrase_count(emails, phrase_2)
    print(f"Phrase 2 ('{phrase_2}') count: {phrase_2_count}")