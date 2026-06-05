#\\Write a Python Program (W.P.P.) to allow online exam access only if:
#Student is registered.Fees are paid.            
#System time is within the exam window.
#If the student is not registered, access is denied.
#If the student is registered but fees are not paid, access is denied.
#If fees are paid and time is valid, the exam starts.Otherwise, the exam does not start.8

registered = input("Is student registered? (yes/no): ")
fees_paid = input("Are fees paid? (yes/no): ")
time_valid = input("Is system time within exam window? (yes/no): ")

if (registered != "yes"):
    print("Access Denied")
    
elif (fees_paid != "yes"):
    print("Access Denied")
    
elif (time_valid == "yes"):
    print("Exam Started")
else:
    
    print("Exam Not Started")