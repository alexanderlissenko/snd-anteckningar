#!/usr/bin/env python
from pyPdf import PdfFileWriter, PdfFileReader
import imaplib

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('dtekanteckningar@gmail.com', 'anteckningar')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.

result, data = mail.search(None, "ALL")
 
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest
 
result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
email_attachment = data[0][1] # here's the body, which is raw text of the whole email
# including headers and alternate payloads

f = open('testmail.pdf', 'w+')
f.write(email_attachment)

print(email_attachment)