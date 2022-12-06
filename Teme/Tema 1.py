'''
1)
O variabila este o zona din memorie care tine date ( un loc unde stocam valori )
'''

#2)
x = "Robert"         #String
y = 20               #Integer
populatie = 19.23    #Double
ok = True            #Boolean

#3)
print(type(x))            #<class 'str'>
print(type(y))            #<class 'int'>
print(type(populatie))    #<class 'float'>
print(type(ok))           #<class 'bool'>

#4)
populatie = round(populatie)    #19.23 va deveni 19
print(populatie)                #19
print(type(populatie))          #<class 'int'>

#5)
print(f"Ma numesc {x}.")
print(f"Am {y} de ani.")
print(f"Populatia Romaniei, ca numar intreg, este de {populatie} milioane de locuitori.")
print(f"La proba de aseara, Liviu a mers pe optiunea {ok}.")

#6)
nume = input("Alege un nume: ")                    #Tanase
prenume = input('Alege un prenume: ')              #Robert
z = len(nume+prenume)                              #12
print(f"Numele complet are {z} elemente.")         #Numele complet are 12 elemente.

#7)
lungimea = int(input("Alegeti dimensiunea lungimii: "))     #fortam variabila 'lungimea' sa fie de tip int
latimea = int(input("Alegeti dimensiuena latimii: "))       #fortam variabila 'latimea' sa fie de tip int
arie = lungimea * latimea
print(f"Aria dreptunghiului este: {arie}.")

#8)
citat = "Coral is either the stupidest animal or the smartest rock"
print(citat.count("the"))               #functie ce numara aparitiile sirului 'the'

#9)
citat = "Coral is either the stupidest animal or the smartest rock"
print(citat.replace("the", "THE"))      #functie ce inlocuieste orice sir "the" cu sirul "THE"

#10)
adevar = citat.isnumeric()              #functie ce ne va indica True/False daca in sirul "citat" toate caracterele sunt numere
assert adevar == False                  #il intreb pe Python: Hey, adevar este fals
print("Sirul nu contine doar cifre")    #modalitate de a verifica daca propozitia este evaluata in final cu Truc

#11)
sir = input("Introduceti un sir: ")
q = len(sir)                            #functie ce determina lungimea unui sir
if q % 2 == 0:
    print("Par")
else:
    print("Impar")
    print(sir[(q-1)//2:(q+2)//2])

#12)
def estePalindrom(sir):                 #functie ce va crea ,oglinditul' sirului nostru
    return sir == sir[::-1]
palindrom = estePalindrom(sir)          #utilizam functia pentru a crea ,oglinda' sirului nostru
if palindrom:
    print("Sirul este palindrom")
else:
    print("Sirul nu este palindrom")