# Create employee dictionary and perform simple operation.
employee = {}

employee["id"] = int(input("Enter Employee ID: "))
employee["name"] = input("Enter Employee Name: ")
employee["age"] = int(input("Enter Employee Age: "))

employee["name"] = "Kiran"

print(employee)


for i in employee:
    print(i, ":",)


for k, (key, value) in enumerate(employee.items()):
    print(k, key, ":", value)
    
del employee['name']
print(employee)    
