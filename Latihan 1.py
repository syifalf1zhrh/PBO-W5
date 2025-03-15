class Kucing:
    def suara(self):
        return "Meong"

class Anjing:
    def suara(self):
        return "Guk guk"

class Sapi:
    def suara(self):
        return "Moo"

def cetak_suara(hewan):
    return hewan.suara()

hewan1 = Kucing()
hewan2 = Anjing()
hewan3 = Sapi()

print ("\nSuara Kucing adalah", cetak_suara(hewan1))
print ("Suara Anjing adalah", cetak_suara(hewan2))
print ("Suara Sapi adalah", cetak_suara(hewan3))  