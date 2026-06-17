#write a python program to create student with instance variable student name,student id,student mob no, accept and print the details for one student.
class Student:
    def accept(self):
        self.name = "abc"
        self.id = 123
        self.mobno = 1234567890

    def print_details(self):
        print("Name :", self.name)
        print("ID :", self.id)
        print("Mobile No :", self.mobno)

s1 = Student()
s1.accept()
s1.print_details()