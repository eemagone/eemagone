class Darbinieks():

    def __init__(self, vards, uzvards, nostradatas_h):
        self.vards = vards
        self.uzvards = uzvards
        self.nostradatas_h = nostradatas_h

    def aprekinat_algu(self, likme):
        self.nostradatas_h = self.nostradatas_h * likme 
        print(f"Alga: {self.nostradatas_h}$")

    def radit_info(self):
        print(f"Darbinieka vārds n uzvārds: {self.vards}, {self.uzvards}")


class BirojaDarbinieks(Darbinieks):

    def __init__(self, vards, uzvards, nostradatas_h, kabineta_nr):
        super().__init__(vards, uzvards, nostradatas_h)
        self.kabineta_nr = kabineta_nr

    def radit_info(self):
        print(f"Vards: {self.vards}, uzvards: {self.uzvards}, kabinets: {self.kabineta_nr}")


class Programmetajs(Darbinieks):

    def __init__(self, vards, uzvards, nostradatas_h, valodas):
        super().__init__(vards, uzvards, nostradatas_h)
        self.valodas = valodas

    def radit_info(self):
        print(f"Programmētāja vārds: {self.vards}, uzvards: {self.uzvards}, programmesanas valodas: {self.valodas}")


darbinieks1 = BirojaDarbinieks("Jekabs", "Laizans", 100, 103)
darbinieks2 = Programmetajs("Arturs", "Kurmahins", 200, ["Python", "C++"])

darbinieks1.radit_info()
darbinieks2.radit_info()


darbinieks1.aprekinat_algu(5.7)
darbinieks2.aprekinat_algu(4)