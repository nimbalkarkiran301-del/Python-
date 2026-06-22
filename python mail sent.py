# smtplib → Connects to the mail server.
# EmailMessage → Creates the email.


import smtplib
from email.message import EmailMessage

# Create Email Object
msg = EmailMessage()

# Email Headers
msg["Subject"] = "Python Test Mail"
msg["From"] = "nimbalkarkiran301@gmail.com"
msg["To"] = "nimbalkarkiran301@gmail.com"

# Email Body
msg.set_content("""
<h1>Hello Student</h1>

This email is sent using Python's modern EmailMessage class.

Regards,
Python Program
""", subtype="html",)

# Connect to Gmail SMTP Server
server = smtplib.SMTP("smtp.gmail.com", 587)

# Start Secure Connection
server.starttls()

# Login using App Password
server.login(
    "nimbalkarkiran301@gmail.com",
    "rpxn csqs odrf rrth"
)

# Send Email
server.send_message(msg)

print("Email Sent Successfully!")

# Close Connection
server.quit()