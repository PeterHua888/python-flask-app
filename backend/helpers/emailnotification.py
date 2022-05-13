from email.mime.text import MIMEText
import smtplib
#SERVER = "localhost"

class EmailNotification:
    def __init__(self, detail, service, server):
        self.detail = detail
        self.service = service
        self.server = server

    def send(self):
        FROM = ''
        password = ''

        TO = ["systems@kenshodata.com.au"] # must be a list

        SUBJECT = "[%s Server] Auto-BETFAIR Exception Notification!" % (self.server)

        TEXT = """
        VM: 

        Which Service: 

        Which Function: %s

        Details are as follows:
        %s
        """

        # Prepare actual message
        message = MIMEText(TEXT % (self.service, self.detail))
        message["Subject"] = SUBJECT
        message["From"] = FROM
        message["To"] = ", ".join(TO)

        # Send the mail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(FROM, password)
        # print("Login success")
        server.sendmail(FROM, TO, message.as_string())
        # print("Email sent")
        server.quit()
