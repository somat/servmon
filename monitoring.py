import os
import re
import time
import smtplib

class Monitoring:
    def __init__(self, hosts, smtpuser, smtppasswd, fromaddr, toaddr):
        lifeline = re.compile(r"(\d) received")
        print time.ctime()
        
        for host in hosts:
            check = os.popen("ping -q -c2 "+host,"r")
            while 1:
                line = check.readline()
                if not line: break
                result = re.findall(lifeline,line)
                if result:
                    if int(result[0]) == 0:
                        print "\nSending email ..."
                        subject = "Mesin %s tidak terjangkau" % (host)
                        content = "Mesin %s tidak terjangkau" % (host)
                        self.sendmail(smtpuser, smtppasswd, fromaddr, toaddr, subject, content)

    def sendmail(self, username, password, fromaddr, toaddr, subject, content):
        msg = """From: %s
To: %s
Subject: %s

%s
        """ % (fromaddr, toaddr, subject, content)
        
        server = smtplib.SMTP('smtp.server:port')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddr, msg)
        server.quit()

if __name__ == "__main__":
    hosts = ["", "", ""]
    smtpuser = ""
    smtppasswd = ""
    fromaddr = ""
    toaddr = ""
    monitor = Monitoring(hosts, smtpuser, smtppasswd, fromaddr, toaddr)

