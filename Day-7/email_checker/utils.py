import email
from email.header import decode_header


def get_mail_count(mail, folder):
    _, messages = mail.select(folder)

    return int(messages[0])


def get_latest_emails(mail, msg_count, count):
    emails = []
    for i in range(msg_count, msg_count - count, -1):
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

                emails.append({"from": mail_from, "subject": subject, "content": body})

    return emails


def get_phrase_count(emails, phrase):
    count = 0

    for email in emails:
        if phrase.lower() in email["content"].lower():
            count += 1

    return count
