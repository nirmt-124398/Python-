# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    sq=0
    cube=0
    sqroot=0
    def __init__(self,n):
        self.sq=n**2
        self.cube=n**3
        self.sqroot=n**1/2
    def print(self):
        print(f"Square: {self.sq}\n Cube: {self.cube}\nSquareroot: {self.sqroot}")

c=Calculator(4)
c.print()