class Transportlidzeklis():
    
    def __init__(self, razotajs, modelis, max_atrums):
        self.razotajs = razotajs
        self.modelis = modelis
        self.max_atrums = max_atrums

    def paradit_datus(self):
        print(f"Razotajs: {self.razotajs},\nmodelis: {self.razotajs},\nmaksimalais atrums: {self.max_atrums}km/h")

    
class Automobilis(Transportlidzeklis):

    def __init__(self, razotajs, modelis, max_atrums, degvielas_tilpums):
        super().__init__(razotajs, modelis, max_atrums)
        self.degvielas_tilpums = degvielas_tilpums

    def paradit_datus(self):
        super().paradit_datus() 
        print(f"degvielas tilpums: {self.degvielas_tilpums} L")

class Elektroskrejritenis(Transportlidzeklis):

    def __init__(self, razotajs, modelis, max_atrums, baterijas_ietilpiba):
        super().__init__(razotajs, modelis, max_atrums)
        self.baterijas_ietilpiba = baterijas_ietilpiba

    def paradit_datus(self):
        super().paradit_datus()
        print(f"baterijas ietilpība: {self.baterijas_ietilpiba} kWh")

transports1 = Automobilis("BMW", "X5", 270, 90)
transports2 = Elektroskrejritenis("Skoda", "passat", 9999, 1.9)

transports1.paradit_datus()
print("")
transports2.paradit_datus()