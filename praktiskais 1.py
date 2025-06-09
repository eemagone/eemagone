class Gramata():

    def __init__(self, nosaukums, autors, lpp_skaits):
        self.nosaukums = nosaukums
        self.autors = autors
        self.lpp_skaits = lpp_skaits

    def paradit_info(self):
        print (f"Grāmatas nos.: {self.nosaukums}, autors: {self.autors}, lpp skaits: {self.lpp_skaits}")

a = input(f"Grāmatas nosaukums: ")
b = input(f"Autors: ")
c = input(f"Lapaspusu skaits: ")

cilveks1 = Gramata(a, b, c)
cilveks1.paradit_info()