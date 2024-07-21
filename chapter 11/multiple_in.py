class Employee:
    name="Nirmit"
    company="ITC"
    def show(self):
        print(f"name of the Emplyee is {self.name} ")


class Coder:
    
    def salary(self):
        print(f"and His company is {self.company}.")

class Programmer(Employee,Coder):
    language='python'
    def lang(self):
        print(f'and his favourate language is {self.language}')

p=Programmer()
p.show()
p.salary()
p.lang()