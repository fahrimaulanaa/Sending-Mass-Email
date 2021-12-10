import csv
import smtplib
from email.mime.text import MIMEText
import re

fp = open('message.txt', 'rb')
msg = MIMEText(fp.read())
fp.close
msg['Subject'] = 'Testing'
msg['From'] = 'fahri_ghazali_30rpl@student.smktelkom-mlg.sch.id'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('fahri_ghazali_30rpl@student.smktelkom-mlg.sch.id', 'pktt4553')
email_data = csv.reader(open('email.csv', 'rb'))
email_pattern = re.compile('"^.+@.+\..+$')
for row in email_data:
    if( email_pattern.search(row[1]) ):
        del msg['To']
        msg['To'] = row[1]
        try:
            server.sendmail('fahrimaulanaa127@gmail.com', [row[1]], msg.as_string())
        except smtplib.SMTPException:
            print("An error occured.")
server.quit()