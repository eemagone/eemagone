class Darbinieks:

    def __init__(self, vards, uzvards):
        self.vards = vards
        self.uzvards = uzvards

    def __repr__(self):
        return f"{self.vards}, {self.uzvards}"
    
    def sasveicinaties(self, sveiciens):
        print(f"Sveiks,{sveiciens} {self.vards}")


darbinieks1 = Darbinieks("Yo", "BBO")
print(darbinieks1)

darbinieks1.sasveicinaties("lielais")