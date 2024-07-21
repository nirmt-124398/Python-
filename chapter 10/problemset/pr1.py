# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company="Microsoft"
    name=""
    age=0
    salary=0

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def print(self):
        print(f"Name: {self.name}\nAge: {self.age}\nSalary: {self.salary}")
p=Programmer("Nirmit Rampal",20,1200000000000)
p.print()
q=Programmer("akash",19,12000000)
q.print()