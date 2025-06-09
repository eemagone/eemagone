class BankasKonts():

    def __init__(self, ipasnieks, bilance):
        self.ipasnieks = ipasnieks
        self.bilance = bilance

    def paradit_bilanci(self):
        print(f"Konta ipasnieks: {self.ipasnieks}, konta bilance: {self.bilance}")

    def ieskaitit(self, summa):
        self.bilance += summa 
        print(f"Pievienots {summa}$ kontam")

    def iznemt(self, summa):
        self.bilance -= summa
        print(f"Atņemts {summa}$ kontam")

a = BankasKonts("Juris", 100)
a.ieskaitit(20)
a.iznemt(30)
a.paradit_bilanci()