# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways.

from random import randint
class Train:
    def __init__(self,trainNo,frm,to):
        self.trainNo=trainNo
        self.frm=frm
        self.to=to

    def book(self):
        print(f"Train BOOKED\nINFO:\n{self.trainNo}\n{self.frm}\n{self.to}")
    def status(self):
        print(f"Train {self.trainNo} is on time.")
    def fare(self):
        print(f"Ticket fare: {randint(1000,10000)}")

t=Train(12334,"Ludhiana","patiala")
t.book()
t.status()
t.fare()

# Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf” or “harry” and see the effects.-- No as long as all self are changed