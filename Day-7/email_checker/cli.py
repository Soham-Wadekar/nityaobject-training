import argparse
from email_checker.connection import connect_to_email
from email_checker.utils import get_mail_count, get_latest_emails, get_phrase_count


def main():
    parser = argparse.ArgumentParser(description="Email Checker CLI")
    parser.add_argument(
        "--folder", default="INBOX", help="Mailbox folder to use (default: INBOX)"
    )
    parser.add_argument("--count", action="store_true", help="Get mail count")
    parser.add_argument("--latest", type=int, metavar="N", help="Get N latest emails")
    parser.add_argument(
        "--phrase", type=str, metavar="PHRASE", help="Search for a specified phrase"
    )

    args = parser.parse_args()

    mail = connect_to_email()

    msg_count = get_mail_count(mail, args.folder)

    if mail:
        print(f"Connected to mail!")

    if args.count:
        print(f"Total Mail Count: {msg_count}")

    emails = []
    if args.latest:
        emails = get_latest_emails(mail, msg_count, args.latest)
        print(f"Latest {args.latest} emails from '{args.folder}':")
        for i, email in enumerate(emails, 1):
            print(f"{i}. From: {email['from']}, Subject: {email['subject']}")

    if args.phrase:
        if not emails:
            emails = get_latest_emails(mail, msg_count, 50)
        phrase_count = get_phrase_count(emails, args.phrase)
        print(
            f"Phrase '{args.phrase}' found {phrase_count} times in last {len(emails)} emails"
        )


if __name__ == "__main__":
    main()
