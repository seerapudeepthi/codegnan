SMTP(simple mail transfer protocol):
    this is used to send emails from server to server
note:
1.SMTP SSL PORT:
------------------
465

2.SMTP TLS PORT:
------------------
587

import smtplib

EmailMessage class:
--------------------
msg['Subject']='SMTP ON Mail'
msg['From']='sender@mail.com'
msg['To']='receiver@mail.com
_____________________________________________________________________________________________
import smtplib
from email.message import EmailMessage
sender = "deepthiseerapu2004@gmail.com"
password = 'rnnqtkugxlweruud'
msg = EmailMessage()
msg['subject']='welcome mail'
msg['From']= sender
msg['To']= 'reshmanaguru30@gmail.com'

msg.set_content('your instagram account has hacked')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()
________________________________________________________________________________________________

import smtplib
from email.message import EmailMessage
sender = 'deepthiseerapu2004@gmail.com'
password = 'rhcydcmgfybrcbkt'
receiver = ['reshmanaguru30@gmail.com','kavs14345@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in receiver:
    msg = EmailMessage()
    msg['subject']='welcome mail'
    msg['From']= sender
    msg['To']= email
    msg.set_content('reshma approach explain cheyyandi')
    server.send_message(msg)
server.quit()
    
