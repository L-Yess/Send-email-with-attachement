
# import time
# from   threading import Thread
# import ssl
import smtplib as smtplib
from   email.mime.multipart import MIMEMultipart
from   email.mime.base import MIMEBase
from   email.mime.text import MIMEText
from   email.utils import formatdate
from   email import encoders

def send_email_att(subject,filename):

	FROM='example1@email.com'
	TO  ='example2@email.com'
	PWD='PasswordOfThe<From>Email'

	# STMP server (gmail, yahoo etc..)
	SERVER="smtp.gmail.com"
	PORT=587
	msg = MIMEMultipart()
	msg['Subject'] = subject
	msg['From'] = FROM
	msg['To'] = TO
	msg.preamble = "test" 
	part = MIMEBase('application', "octet-stream")
	part.set_payload(open(filename, "rb").read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="any_name.txt"')
	msg.attach(part)
	try:
		s = smtplib.SMTP(SERVER, PORT)
		s.ehlo()
		s.starttls()
		s.ehlo()

		s.login(user = EMAIL, password = PWD)
		s.sendmail(FROM, TO, msg.as_string())
		s.quit()
		print ("done!")
		return True
	except :
		print ("Error")
		return False

send_email_att("Subject","Path/to/the/file.txt")