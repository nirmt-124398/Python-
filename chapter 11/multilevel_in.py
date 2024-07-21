class Employee:
    name="Nirmit"
    def nme(self):
        print(f"Employee name is {self.name}.")

class Coder(Employee):
    Language="PYTHON"
    def lang(self):
        print(f"And his fav language is {self.Language}")

class manager(Coder):
    project_type="Website"
    def pro_type(self):
        print(f"And his project type {self.project_type}")

a=manager()
a.nme()
a.lang()
a.pro_type()