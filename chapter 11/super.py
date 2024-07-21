class Employee:
    def __init__(self):
        print('I am Employee')

class Coder(Employee):
    def __init__(self):
        super().__init__()
        print('I am Coder')

class manager(Coder):
    def __init__(self):
        super().__init__()
        print('I am manager')

m=manager()
