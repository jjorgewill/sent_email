import smtplib
fromaddr = 'email_usuario_receptor@dominio'
toaddrs  = 'email_usuario_emisor@dominio'
msg = 'Correo enviado utilizano Python + smtplib'
username = 'correo@dominio'
password = 'contrasena' 
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg) 
server.quit()

