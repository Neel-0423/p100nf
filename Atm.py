amt = 10000
class Atm():
    def __init__(self,acn,pn):
        self.acn=acn
        self.pn=pn
    def balanceEnquiry(self):
        print("your balance is "+ amt)
    def cashWithdrawl(self):
        wa = input("how much ammount do you want to withdraw")
        amt = amt-wa
        print("withdrawl complete")
        print("remaining balance is "+ amt)
def play():
    person=Atm("45776834","57324789")
    person.balanceEnquiry()
    person.cashWithdrawl()
    print(person.acn)
    print(person.pn)
play()



