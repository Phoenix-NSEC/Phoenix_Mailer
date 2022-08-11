import os
import smtplib
from smtplib import SMTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from string import Template
load_dotenv('./configs/.env')

'''Configs'''
zohoHost = os.getenv('ZOHO_HOST')
senderEmail = os.getenv('ZOHO_EMAIL')
senderPassword = os.getenv('ZOHO_PASSWORD')
replyEmail = os.getenv('REPLY_EMAIL')



def sendZohoMail(name,subject,email):
    msg = MIMEMultipart()
    msg['Subject'] = subject  # SUBJECT
    msg['From'] = 'PHOENIX - Official Tech Club of NSEC <no-reply@phoenixnsec.in>'
    msg['reply-to'] = replyEmail
    s = open('./assets/mail.html').read()
    html = Template(s).safe_substitute(name=name)
    txt = MIMEText(html, 'html')
    msg.attach(txt)
    try:
        del msg['To']
        msg['To'] = email
        """Setting of mailing Server"""
        server = smtplib.SMTP(zohoHost)
        server.starttls()
        server.login(senderEmail, senderPassword)
        server.sendmail(senderEmail, [email], msg.as_string())
        print("sent to" + " "+name)
        server.quit()
        return 1   
    except SMTPException:
        print("Failed for " + name)
        return 0  
    

if __name__ == "__main__":
    print("Zoho Mail Sender")