# Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute? -- YES ---HOW[below]

class Some:
    a=20
    def print(self):
        print(f"a: {self.a}")

q=Some()
q.print()
q.a=0
q.print()