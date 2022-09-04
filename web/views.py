from email.message import EmailMessage
from flask import Blueprint, request, render_template, redirect, flash
from markupsafe import escape
from .conf import sender, password
import re
import smtplib
import ssl

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def index():
	return redirect('/send-email')


@views.route('/send-email', methods=['GET', 'POST'])
def send_email():
	if request.method == 'POST':
		receiver = request.form['receiver']
		subject = request.form['subject']
		message = request.form['message']

		pattern = '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$'
		if re.search(pattern, receiver):
			em = EmailMessage()
			em.add_header('From', sender)
			em.add_header('To', receiver)
			em.add_header('Subject', subject)
			em.set_content(message)

			context = ssl.create_default_context()

			with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465, context=context) as smtp:
				smtp.login(sender, password)
				smtp.sendmail(sender, receiver, em.as_string())
				print('siccess')
				return redirect('/email-sent')

	return render_template('sendmail.html')


@views.route('/email-sent', methods=['GET', 'POST'])
def sucess():
	if request.method == 'POST':
		return redirect('/send-email')

	return render_template('sendsuccess.html')

# TODO: Add functionality to attachment
# TODO: Handle errors when sending of email