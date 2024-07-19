import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Example usage
sender_email = "carecompass5@gmail.com"
# receiver_email = "carecompass5@gmail.com"
password = "tgkr prmo rdqn stgy"


def send_mail(user_email,username,user_lastname, message,receiver_email):
     
  with smtplib.SMTP("smtp.gmail.com", 587) as server:
      server.starttls()
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)
      

    