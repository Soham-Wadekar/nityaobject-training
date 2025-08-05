# Day 1 Log

### PROBLEM STATEMENT
| Write a Python program to read from a mailbox and print how many emails are available in the "Inbox" or a specific folder. Among the last five emails, how many contain the phrase "in response to your marketing email"? How many contain the response "unsubscribe service"?

**METHODOLOGY**
1. Connect and create an instance to access mail using `IMAP_SERVER` and login credentials
2. Get the status code and message count using `.select(folder_name)` command
3. Decode and parse through mails to make them human-readable (`get_latest_emails()`)
4. Match phrase (can be done using `re` for better searching)

**WHAT I LEARNED**
1. Connecting to a mail service account using `imaplib`
2. Functions to access and decode emails

**REFERENCE MATERIAL**
https://thepythoncode.com/article/reading-emails-in-python
