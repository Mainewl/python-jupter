import smtplib

email = "manonhaas.s2@gmail.com"
receeiver_address = "eduardo.gomes@schaeferyachts.com.br"
senha = "fmyoukbquxxfkzgx"

subject = "codigo funcionando"
body = "Fazendo um teste pra ver como fica esse email \n\ntomara que fique bom"

smtp_server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtp_server.login("manonhaas.s2@gmail.com", "fmyoukbquxxfkzgx")

message = f"subject: {subject}\n\n{body}"

smtp_server.sendmail(email, receeiver_address, message)

smtp_server.close()

#^OK^
