import time
import smtplib
from email.mime.text import MIMEText

#Send text file from "addr" to "addr"
def upload_mail(addr, file):
	try:
		f = open(textfile, 'rb')
		#create message
		msg = MIMEText(f.read())
	finally:
		f.close()
	msg['Subject'] = 'Log'
	msg['From'] = addr
	msg['To'] = addr
	try:
		server = smtplib.SMTP('localhost')
		server.sendmail(addr, [addr], msg.as_string())
	finally:
		server.quit()

if __name__ == "__main__":
	t = time.time()
	while True:
		#if 2 or more hours have passed send log file for the day
		if time.time() - t >= 3600:
			upload_mail(ADDR, FILE)
		else:
			#wait to send
			time.sleep(120)