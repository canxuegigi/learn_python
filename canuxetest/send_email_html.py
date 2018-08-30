#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'canxuegigi@163.com'
password = 'mll123XSG'
receiver = 'zhengjing@lixin360.com'
subject = 'subject'
smtp_server = 'smtp.163.com'
body = "<html><body>I'm email body</body></html>"
msg_text = MIMEText(body, 'html', 'utf-8')
msg_text['Subject'] = Header('我是谁', 'utf-8')
msg_text["From"] = sender
msg_text["to"] = receiver

smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(sender, password)
smtp.sendmail(sender, receiver, msg_text.as_string())











