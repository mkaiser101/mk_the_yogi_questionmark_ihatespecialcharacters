from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl, pickle, base64, sys

smtp_server = "smtp.gmail.com"
sender = "mk.the.yogi@gmail.com"
reciever = "mkaiser101@gmail.com"
port = 465


message = MIMEMultipart()
message["To"] = reciever
message["Subject"] = "testing email alerts via cron"
message.attach(MIMEText("This was a test"))
context = ssl.create_default_context()

if sys.argv[1]:
    creds = sys.argv[1]
    with open(creds, 'rb') as readfile:
        auth_list = pickle.load(readfile)
    password = base64.decodebytes(auth_list)
    password = password.decode("utf-8") 


else:
    with open("creds.bin", 'rb') as readfile:
        auth_list = pickle.load(readfile)
    password = base64.decodebytes(auth_list)
    password = password.decode("utf-8") 


try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender, str(password))
        server.sendmail(sender, reciever, message.as_string())

except Exception as e:
    print(str(e))


