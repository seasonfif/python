#!usr/bin/env python
# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.163.com"
mail_user="mobilepackage@163.com"
mail_pass="1mobilepackage"

sender = "mobilepackage@163.com"
receivers = ["zhangqiang01@lianjia.com"]
subject = '邮件标题：自动打包'
message = MIMEText("只要大家把邮件的标题和内容写的正规点(像平常写邮件一样),就不会出现这种情况了邮件标题：自动打包content", 'plain', 'utf-8')
message['From'] = Header(sender, 'utf-8')
message['To'] =  Header("package", 'utf-8')
message['Subject'] = Header(subject, 'utf-8')
try:
	smtpObj = smtplib.SMTP_SSL()
	smtpObj.connect(mail_host, 994)
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, message.as_string())
	smtpObj.close
	print "邮件发送成功"
except smtplib.SMTPException, e:
	print e
	print "Error: 无法发送邮件"