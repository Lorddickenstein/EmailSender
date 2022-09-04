# Before running this program, follow these instructions first:


# Set up your 2-Step Verification on gmail: 
	# Manage your google accout>Security>Signin in to Google
# Go to App passwords, input your gmail passwords to confirm it's you,
	# then Select app>Mail, select other device (custom name) and put 'python' or any other name
# Click GENERATE and make sure that you copy the generated code
# Add the code to your environmental variable or even better if you use venv by python


# You can test this using a temporary email receiver by going to temp-mail.org

from email.message import EmailMessage
import os
import re
import smtplib
import ssl


def verify_email(email):
	# source: https://pythonsansar.com/how-to-verify-email-in-python/
	pattern = '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'
	return re.search(pattern, email)


def send_email(receiver, subject, message):
	sender = os.getenv('SECRET1')
	password = os.getenv('SECRET2')

	em = EmailMessage()
	em.add_header('From', sender)
	em.add_header('To', receiver)
	em.add_header('Subject', subject)
	em.set_content(message)

	context = ssl.create_default_context()

	with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=context) as smtp:
		smtp.login(sender, password)
		smtp.sendmail(sender, receiver, em.as_string())
		print('Email has been sent!')
		return

	return 'Error. Something went wrong.'


if __name__ == "__main__":
	print("Enter receiver: ", end='')
	receiver = input()
	print("Enter subject: ", end='')
	subject = input()
	print("What's the message?")
	message = input()

	if verify_email(receiver):
		send_email(receiver, subject, message)
	else:
		print('Email given is invalid.')