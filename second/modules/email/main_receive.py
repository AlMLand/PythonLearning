import getpass
import imaplib

with imaplib.IMAP4_SSL('imap.gmail.com') as imap4_obj:
    email = getpass.getpass('Email: ')
    password = getpass.getpass('Password: ')
    imap4_obj.login(email, password)

    # This will list all the folders in the email account
    print(imap4_obj.list())
    imap4_obj.select('inbox')
    typ, data = imap4_obj.search(None, 'SINCE', '03-Mar-2025')
    for num in data[0].split():
        typ, data = imap4_obj.fetch(num, '(RFC822)')
        if data:
            print(f"Message {num}\n{data[0][1].decode('utf-8')}\n")
