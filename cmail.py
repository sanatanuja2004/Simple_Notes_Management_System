app_password="awzn cisp pmay unjd"
import smtplib
from email.message import EmailMessage    # EmailMesssage is a class which is used to define email format
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)    # server -> object, 465 -> port number 
    server.login("sanatanuja2004@gmail.com",app_password)   
    msg=EmailMessage()   # obj for EmailMessage
    msg["FROM"]="santanuja2004@gmail.com"   # FROM -> attribute
    msg["SUBJECT"]=subject   # defined in function
    msg["TO"]=to   # defined in function
    msg.set_content(body)   # method
    server.send_message(msg)   # send_message -> method
    server.close()   # closing server object (optional)

