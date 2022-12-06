#1)
class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere(self):
        print(self.raza)
        print(self.culoare)

    def aria(self):
        return 3.14 * self.raza * self.raza

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return 2 * 3.14 * self.raza


Ianis = Cerc(5, "alb")
Ianis.descriere()
print(Ianis.aria())
print(Ianis.diametru())
print(Ianis.circumferinta())

Razvan = Cerc(4, "negru")
Razvan.descriere()
print(Razvan.aria())
print(Razvan.diametru())
print(Razvan.circumferinta())

print("\r")

#2)
'''
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
'''

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        print(self.lungime)
        print(self.latime)
        print(self.culoare)

    def aria(self):
        return self.latime * self.lungime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare
        print(self.culoare)

Valentin = Dreptunghi(5, 4, "rosu")
Valentin.descrie()
print(Valentin.aria())
print(Valentin.perimetru())
Valentin.schimba_culoarea("verde")

Denis = Dreptunghi(6, 3, "albastru")
Denis.descrie()
print(Denis.aria())
print(Denis.perimetru())
Denis.schimba_culoarea("galben")

print("\r")

#3)
class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(self.nume)
        print(self.prenume)
        print(self.salariu)

    def nume_complet(self):
        return self.nume + " " + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        return (1 + procent) * self.salariu

Numar7 = Angajat("Alex", "Chipciu", 1000)
Numar7.descrie()
print(Numar7.nume_complet())
print(Numar7.salariu_lunar())
print(Numar7.salariu_anual())
print(Numar7.marire_salariu(0.25))

Numar10 = Angajat("Cristi", "Tanase", 2000)
Numar10.descrie()
print(Numar10.nume_complet())
print(Numar10.salariu_lunar())
print(Numar10.salariu_anual())
print(Numar10.marire_salariu(0.5))

print("\r")

#4)
class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.")

    def debitare_cont(self, suma):
        self.sold += suma
        return self.sold

    def creditare_cont(self, suma):
        self.sold -= suma
        return self.sold

bogat = Cont("NL27INGB2922497305", "Arjen Robben", 1000)
bogat.afisare_sold()
print(bogat.debitare_cont(200))
print(bogat.creditare_cont(300))

sarac = Cont("MK88899546744147353", "Goran Pandev", 200)
sarac.afisare_sold()
print(sarac.debitare_cont(100))
print(sarac.creditare_cont(150))

print("\r")

#6)
class Masina:
    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    marca = "BMW"
    viteza_actuala = 0
    culoare = "gri"
    culori_disponibile = {"rosu", "albastru", "verde", "alb", "negru", "portocaliu"}
    inmatriculata = False

    def descrie(self):
        print(Masina.marca)
        print(Masina.viteza_actuala)
        print(Masina.culoare)
        print(Masina.inmatriculata)

    def inmatriculare(self):
        Masina.inmatriculata = True

    def vopseste(self, culoare_noua):
        culori_disponibile = {"rosu", "albastru", "verde", "alb", "negru", "portocaliu"}
        if culoare_noua in culori_disponibile:
            Masina.culoare = culoare_noua
            print(Masina.culoare)
        else:
            print("Eroare. Nu gasim culoarea pe stoc.")

    def accelereaza(self, viteza):
        if viteza < 0:
            print("Eroare. Nu exista aceasta viteza.")
        elif viteza == 0:
            print("Deja ai viteza asta.")
        else:
            if viteza <= self.viteza_maxima:
                Masina.viteza_actuala = viteza            #daca printam aici se afisau o multime de viteze
            print(f"Am {viteza} de km/h.")                #s-a atins viteza dorita
        Masina.viteza_actuala = 0                         #resetam la 0 pentru urmatorul obiect (f10 dupa e90)

    def franeaza(self):
        viteza_actuala = 0
        print("Masina s-a oprit.")

e90 = Masina("Seria 3", 230)
e90.descrie()
e90.inmatriculare()                                       #acum se va schimba inmatricularea in True
e90.descrie()
e90.vopseste("alb")                                       #masina va fi vopsita in alb
e90.accelereaza(130)
e90.franeaza()                                            #masina se va opri

f10 = Masina("Seria 5", 250)
f10.descrie()
f10.inmatriculare()
f10.descrie()
f10.vopseste("rosu")
f10.accelereaza(220)
f10.franeaza()

print("\r")