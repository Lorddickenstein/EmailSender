import os

# Uncomment below codes if you want to put your credentials in this conf file
# sender = 'your email'
# password = 'your google generated password'

# Comment these two if you decide to do the ones above
sender = os.getenv('SECRET1')
password = os.getenv('SECRET2')