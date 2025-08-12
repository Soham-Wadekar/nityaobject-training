from email_checker import (
    connect_to_email,
    get_latest_emails,
    get_phrase_count,
    get_mail_count,
)

if __name__ == "__main__":
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
