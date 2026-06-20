#write a python program to generate a secure pssword of a user defined length the password must be contain at least one uppercase letter, at least one lowercase letter , at least one digit, and at least one special character the remaining character should randomly and print the password
import string 
import random 

length = int(input('Enter length of the password (length>4):'))
upper = random.choice(string.ascii_uppercase)
lower = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)
symbol = random.choice(string.punctuation)

passw = upper+lower+digit+symbol

rem = length-4
r ="". join(random.choices(string.ascii_letters, k=rem))

final_pass = passw + r
print(final_pass)