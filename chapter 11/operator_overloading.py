class Number():
    def __init__(self,n):
        self.n=n
    def __add__(self,o):
        return self.n + o.n
    
a=Number(1)
b=Number(2)

print(a+b)