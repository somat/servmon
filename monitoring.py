import os
import re
import time
import smtplib

class Monitoring:
    def __init__(self, ip, smtpuser, smtppasswd, fromaddr, toaddr):
        lifeline = re.compile(r"(\d) received")
        check = os.popen("ping -q -c2 "+ip,"r")
        print time.ctime()

        while 1:
            line = check.readline()
            if not line: break
            igot = re.findall(lifeline,line)
            if igot:
                if int(igot[0]) == 0:
                    print "\nSending email ..."
                    subject = "Mesin %s tidak terjangkau" % (ip)
                    content = "Mesin %s tidak terjangkau" % (ip)
                    self.sendmail(smtpuser, smtppasswd, fromaddr, toaddr, subject, content)

    def sendmail(self, username, password, fromaddr, toaddr, subject, content):
        msg = """From: %s
To: %s
Subject: %s

%s
        """ % (fromaddr, toaddr, subject, content)
        
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddr, msg)
        server.quit()

if __name__ == "__main__":
    ip = ""
    smtpuser = ""
    smtppasswd = ""
    fromaddr = ""
    toaddr = ""
    monitor = Monitoring(ip, smtpuser, smtppasswd, fromaddr, toaddr)

