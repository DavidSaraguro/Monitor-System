# File Name: NotificationManager.py
# Summary: This file contains the function send_email.
# Description: Through the smtplib library, alarm notifications are sent to the user's email. 
# Author: David Saraguro Fárez.
# Last Modified: 06-05-2022

import smtplib
from email.message import EmailMessage

class EmailNotifier:
    def __init__(self) -> None:
        pass       



    # Function Name: send_email
    # Description: The content of the email sent from senderaddress@gmail.com to the user is specified.
    # Parameters: failures
    # Returns: None
    
    def send_email(self,failures):
        try:
            email_subject = "WARNING: Radiobase error" 
            sender_email_address = "senderaddress@gmail.com" 
            receiver_email_address = "receiberaddress@gmail.com" 
            email_smtp = "smtp.gmail.com" 
            email_password = "xxxxxxxx" 

            # Create an email message object 
            email_notifier = EmailMessage() 

            # Configure email headers 
            email_notifier['Subject'] = email_subject 
            email_notifier['From'] = sender_email_address 
            email_notifier['To'] = receiver_email_address 

            # Set email body text 
            email_notifier.set_content("Failures in --> " + str(failures)) 

            # Set smtp server and port 
            server = smtplib.SMTP(email_smtp, '587') 

            # Identify this client to the SMTP server 
            server.ehlo() 

            # Secure the SMTP connection 
            server.starttls() 

            # Login to email account 
            server.login(sender_email_address, email_password) 

            # Send email 
            server.send_message(email_notifier) 

            # Close connection to server 
            server.quit()

            print("Email sent successfully")

        except:
            print("Error, email was not sent")


if __name__ == '__main__':
    myEmailNotifier=EmailNotifier()

    myEmailNotifier.send_email("failure in rb01")      

