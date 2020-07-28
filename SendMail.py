from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib,validate_email
def send_email(sender_email,sender_pwd,receiver_email,header,body):
    mime = MIMEMultipart("alternatives")
    mime["From"] = sender_email
    mime["To"] = receiver_email
    mime["Subject"] = header
    mime = MIMEText(body , "html")
    try:
        login_token = smtplib.SMTP("smtp.gmail.com" , 587)
        login_token.starttls()
        login_token.login(sender_email,sender_pwd)
        login_token.sendmail(sender_email,receiver_email, mime.as_string())
        login_token.close()
    except Exception as e:
        print("Error occured at: {}".format(e))
        return False
    else:
        return True

    def __doc__():
        docs = """
                    Simple python package for sending emails, parameters in the order sender_email,sender_pwd,receiver_email,header,body
                """
        return docs
