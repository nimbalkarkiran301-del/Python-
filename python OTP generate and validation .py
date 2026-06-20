#write a python program to create six digit OTP number accept OTP from user and validate if OTP is correct then print login successfully. only theree attempt allow to enter a OTP.
import random
otp = random.randint(100000, 999999)

print("Generated OTP is:", otp)   # for testing

attempt = 3

while attempt > 0:
    user_otp = int(input("Enter OTP: "))

    if user_otp == otp:
        print("Login successfully")
        break
    else:
        attempt -= 1
        if attempt > 0:
            print("Wrong OTP! Attempts left:", attempt)
        else:
            print("No attempts left. Access denied!")