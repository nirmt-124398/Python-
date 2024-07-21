class N:
    a=1
    @classmethod
    def print(cls):
        print(f"a in class atrribute is {cls.a}.")

q=N()
q.a=44
q.print()