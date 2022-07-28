
from base64 import decode
import imaplib 
import email
import smtplib
from email.mime.base import MIMEBase
from email import encoders
import email.mime.application
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



#defs imaplib
Imap = imaplib.IMAP4_SSL("imap.gmail.com")
ema = "manonhaas.s2@gmail.com"
sena = "fmyoukbquxxfkzgx"

#defs smtplib
loga = ("manonhaas.s2@gmail.com")
receeiver_address = ("eduardo.gomes@schaeferyachts.com.br")
senha = ("fmyoukbquxxfkzgx")
# subject = "Arquivo xxxxxxx"
# body = "intuito: enviar arquivos por email \n\ninicialmente to misturando dois cods e vendo se funfa."

#log for donwload 
Imap.login("manonhaas.s2@gmail.com", "fmyoukbquxxfkzgx")
Imap.select(mailbox='Inbox', readonly=True)

response, emailid = Imap.search(None,"All")


for num in emailid[0].split():
    #print(num)   

    response, dados = Imap.fetch (num, '(RFC822)')   
    #print(dados)
    

    emailtext = dados[0][1]
    emailtext = emailtext.decode('utf-8')
    emailtext = email.message_from_string(emailtext)
    # print(emailtext)

for part in emailtext.walk():

    if part.get_content_maintype() == 'multipart':
        continue
    if part.get('Content-Disposition') is None:
        continue
    filename = part.get_filename()
    print(filename)

archive = open(filename, 'wb')
archive.write(part.get_payload(decode=True))
archive.close

Imap.logout

#log for sending  smtplib
#log for sending  smtplib
#log for sending  smtplib
#log for sending  smtplib

#log for sending  smtplib
#log for sending  smtplib
#log for sending  smtplib
#log for sending  smtplib

smlib = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smlib.login('manonhaas.s2@gmail.com', 'fmyoukbquxxfkzgx')

corpse = "Resultado da junção dos dois codigos que eu fiz em funcionamento..."

emailmesg = MIMEMultipart()
de = emailmesg ['From'] = "manonhaas.s2@gmail.com"
para = emailmesg ['To'] = "manonha.s2@hotmail.com"
emailmesg ['Subject'] = 'Arquivo final'
emailmesg.attach(MIMEText(corpse, 'Plain'))


caminho = 'C:/Users/APRENDER/Desktop/vsstudio/A2B8A000.xlsx'
attchment = open(caminho, 'rb')

att = MIMEBase('application', 'octet-stream')
att.set_payload(attchment.read())
encoders.encode_base64(att)

att.add_header('Content-Disposition', f'attachment; filename=A2B8A000.xlsx')
attchment.close()


emailmesg.attach(att)
smlib.sendmail(de, para, emailmesg.as_string())
smlib.quit




























# msg = MIMEMultipart()
# msg['Subject'] = ('testando um codigo novo')
# msg['From'] = ("manonhaas.s2@gmail.com")
# msg['To'] = ("manonha.s2@hotmail.com")

# txt = MIMEText('somente testando esse codigo\n\n não sei se vai funcionar mas okok')
# msg.attach(txt)

# filename = 'teste.png'
# fo=open(filename,'rb')
# email.mime.application.MIMEApplication(fo.read(),_subtype="C:/Users/APRENDER/Desktop/teste.png")
# fo.close()

# attach.add_header('Content-Disposition','attachment',filename=filename)
# msg.attach(file)




# message = f"subject: {subject}\n\n{body}"

# smtp_server.sendmail(email, receeiver_address, message)



