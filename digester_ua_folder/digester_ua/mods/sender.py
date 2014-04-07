from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Header import make_header
from email.Utils import formatdate
import smtplib
#server params
server = 'smtp.gmail.com'
port = 587
#mail encoding
icharset = 'cp866'
def sendmail(to, subject, message):
    #authorization data
    username = 'animedigest@gmail.com'
    password = 'konataizumi'
    #message generating
    msg = MIMEMultipart()
    #header
    hdr = make_header([(subject, icharset)])
    #params
    msg['From'] = username
    msg['To'] = to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = hdr
    #message body: encoding->html->cp866
    msg.attach(MIMEText(message, 'html', icharset))
    #connection
    srv = smtplib.SMTP(server, port)
    srv.ehlo()
    #starting ssl
    srv.starttls()
    srv.ehlo()
    #authorization
    srv.login(username, password)
    #sending
    srv.sendmail(username, to, msg.as_string())
    #closing connection
    srv.close()