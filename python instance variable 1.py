#write a python program create class customer with customer name, customer id,customer Email id ,customer mob no. used  constructor to intialize instance variable and print the details.

class Customer:
    
    def __init__(self, name, cid, mail, mob_no):
        self.name = name
        self.id = cid
        self.mail = mail
        self.mob_no = mob_no

    def display(self):
        print("Customer Name :", self.name)
        print("Customer ID   :", self.id)
        print("Customer Mail :", self.mail)
        print("Customer Mob No :", self.mob_no)

c1 = Customer("Kiran", 101, "kiran@gmail.com", "9022392319")
c1.display()