class Varonis():

    def __init__(self, vards, dzivibas, uzbrukuma_speks):
        self.vards = vards
        self.dzivibas = dzivibas
        self.uzbrukuma_speks = uzbrukuma_speks

    def sanemt_bojajumu(self, bojajums):
        self.dzivibas -= bojajums
        if self.dzivibas < 0:
            self.dzivibas = 0

    def uzbrukt(self, merkis):
        print(f"{self.vards} uzbrūk ar standarta uzbrukumu {merkis.vards}")
        merkis.sanemt_bojajumu(self.uzbrukuma_speks)

    def paradit_statusu(self):
        print(f"{self.vards} ir {self.dzivibas} HP!")

    def ir_dzivs(self):
        return self.dzivibas > 0

    def __str__(self):
        return self.vards


class Bruņinieks(Varonis):

    def __init__(self, vards, dzivibas, uzbrukuma_speks, izturiba):
        super().__init__(vards, dzivibas, uzbrukuma_speks)
        self.izturiba = izturiba

    def uzbrukt(self, merkis):
        if self.izturiba >= 10:
            bojajums = self.uzbrukuma_speks * 2
            print(f"{self.vards} dara stipru sitienu {merkis.vards} un nodara {bojajums}!")
            self.izturiba -= 10
            merkis.sanemt_bojajumu(bojajums)
        else:
            super().uzbrukt(merkis)


class Burvis(Varonis):

    def __init__(self, vards, dzivibas, uzbrukuma_speks, mana):
        super().__init__(vards, dzivibas, uzbrukuma_speks)
        self.mana = mana

    def uzbrukt(self, merkis):
        if self.mana >= 20:
            bojajums = self.uzbrukuma_speks + 15
            print(f"{self.vards} veic ugunsbumbas uzbrukumu {merkis.vards} un nodara {bojajums}!")
            self.mana -= 20
            merkis.sanemt_bojajumu(bojajums)
        else:
            self.mana += 5
            print(f"{self.vards} atjauno savu manu!")
            super().uzbrukt(merkis)


# Spēlētāji
bruninieks = Bruņinieks("Nils", 100, 10, 30)
burvis = Burvis("Everita", 70, 5, 50)

# Cīņas sākums
print("Cīņa sākas!\n")
bruninieks.paradit_statusu()
burvis.paradit_statusu()

print("\n" + "-" * 20)

round = 1
while bruninieks.ir_dzivs() and burvis.ir_dzivs():
    print(f"\n     Round {round}\n")

    bruninieks.uzbrukt(burvis)

    if burvis.ir_dzivs():
        burvis.uzbrukt(bruninieks)

    print("\nRound end status:\n")
    bruninieks.paradit_statusu()
    burvis.paradit_statusu()  

    round += 1

print("\n\n        Cīņa beidzas!\n")

if bruninieks.ir_dzivs():
    print(f"Uzvarēja {bruninieks.vards}!")
elif burvis.ir_dzivs():
    print(f"Uzvarēja {burvis.vards}!")
else:
    print("Neizšķirts...")
