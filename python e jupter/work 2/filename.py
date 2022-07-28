from base64 import decode
import imaplib 
import email

Imap = imaplib.IMAP4_SSL("imap.gmail.com")
ema = "manonhaas.s2@gmail.com"
sena = "fmyoukbquxxfkzgx"
Imap.login("manonhaas.s2@gmail.com", "fmyoukbquxxfkzgx")


Imap.select(mailbox='Inbox', readonly=True)

response, emailid = Imap.search(None,"All")
    #print(emailid)

for num in emailid[0].split():
    #print(num)
    response, dados = Imap.fetch (num, '(RFC822)')
    #print(dados)
    emailtext = dados[0][1]
    emailtext = emailtext.decode('utf-8')
    emailtext = email.message_from_string(emailtext)
    print(emailtext)
    