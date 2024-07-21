class Employee:
    name="Nirmit"
    company="ITC"
    def show(self):
        print(f"name of the Emplyee is {self.name} ")


class Programmer(Employee):
    language='python'
    def lang(self):
        print(f'and his favourate language is {self.language}')

p=Programmer()
p.show()
p.lang()