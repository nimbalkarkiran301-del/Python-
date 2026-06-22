import smtplib
from email.message import EmailMessage
from random import randint
from time import *
from qrcode import *
import os
from datetime import datetime

mail = input ("Enter Gmail to send OTP:")       #email input
otp = randint(000000,999999)                    #Generate OTP

msg = EmailMessage()
msg["Subject"] = "OTP"
msg["From"] =  "nimbalkarkiran301@gmail.com"
msg["To"] = "nimbalkarkiran301@gmail.com"
msg.set_content(f"OTP:- {otp}\n Enter OTP within 2 minutes.")

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("nimbalkarkiran301@gmail.com","rpxn csqs odrf rrth")

start_time = server.send_message(msg)
print ("OTP send Successfully to ",mail)        #OTP sent
start_time = time()

attempts = 3
while attempts > 0:

    entered_otp = int(input("Enter OTP: "))  
    curr_time = time()    

    #curr_time = datetime.now().strftime("%H:%M:%S")

    diff = curr_time - start_time  

    if diff > 120:                               # Check OTP expiry  
        print("OTP has expired.")  
        break  

  
    if entered_otp == otp:                       # Check OTP  
        session_id = randint(1000, 9999)  
  

        print("----------QR CODE DATA----------")  
        print()  
        print("Session ID:", session_id)  
        print("Email:", mail)  
        print('Login Time:',datetime.now())
        print("Status: Active")  
        print()  
        qr_data = (f"----------QR CODE DATA---------- \n Session ID : {str(session_id)}\n Email: {mail}\n Login Time : {str(datetime.now())}\n Status : Active")
        qr = make(qr_data)               # Generate QR code     
        qr.save("Qr.png")  


        print("Login successful!")  
        print("QR code generated successfully.")  
      
      
        break  

    else:  
        attempts -= 1  
        print("Incorrect OTP.")  

        if attempts > 0:  
            print("Attempts left:", attempts)  
        else:  
            print("Attempts are over.")
            