#1)
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#a)---for
for i in range(0, len(masini)):
    print(f"Masina mea preferata este {masini[i]}.")
print("Ai terminat a)")
#b)---for each
for masina in masini:
    print(f"Masina mea preferata este {masina}.")
print("Ai terminat b)")
#c)---while
i = 0
while i < len(masini):
    print(f"Masina mea preferata este {masini[i]}.")
    i += 1
print("Ai terminat c)")

#2)
for i in range(0, len(masini)):                            #de la 0 la 8 inclusiv ( 9 valori )
    for i in range(1,len(masini)-1):                       #de la 1 la 7 inclusiv ( 7 valori )
        masini[i] = masini[i].upper()                      #masini[1]...masini[7] vor fi scrise cu majuscule
print(masini)

#3)
for masina in masini:
    if masina == "MERCEDES":
        print("Am gasit masina dorita de dvs.")
        break                                              #se va iesi din loop atunci cand se gaseste MERCEDES
    else:
        print(f"Am gasit masina {masina}. Mai cautam!")

#4)
for masina in masini:
    if masina == "TRABANT" or masina == "LASTUN":
        continue                                           #se va trece peste aceasta faza daca conditia este adevarata
    else:
        print(f"S-ar putea sa va placa masina {masina}.")

#5)
masini_vechi = []                                          #lista este goala
for i in range(0, len(masini)):
    if masini[i] == "TRABANT" or masini[i] == "LASTUN":
        masini_vechi.append(masini[i])                     #lista masini_vechi primeste elementele Lastun si Trabant
        masini[i] = "Tesla"                                #valorile Lastun si Trabant din masini sunt inlocuite cu Tesla
for i in range(0, len(masini)):
    print(f"Masinile noi sunt: {masini[i]}.")
for i in range(0, len(masini_vechi)):
    print(f"Masinile vechi sunt: {masini_vechi[i]}.")

#6)
pret_masini = {'Dacia': 6800, 'Lastun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000}
for x, y in pret_masini.items():                           #x ---> keys
    if y < 15000:                                          #y ---> values
       print(f"Pentru un buget de sub 15000 euro puteti alege masina: {x}.")

#7)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr = 0
for numar in numere:
    if numar == 3:
        nr += 1
print(f"Valoarea 3 apare de {nr} ori.")

#8) --- fara sum
for i in range(1, len(numere)):
    # sir fibonacci ( se va lua range de la 1 pentru ca valoarea numere[0] sa poata fii adaugata la suma )
    numere[i] = numere[i] + numere[i-1]
print(f'Suma elementor este: {numere[i]}.')


#9)
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
maxim = numere[0]
for valori in numere:
    if(valori > maxim):
        maxim = valori
print(f"Elementul maxim este: {maxim}.")

#10)
for i in range(0, len(numere)):
    if numere[i] >= 0:
        numere[i] = (-1) * numere[i]
print(f"Noua lista este: {numere}.")

#11)
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
noua_lista = []

for i in range(0, len(alte_numere)):
    if alte_numere[i] >= 0:
        numere_pozitive.append(alte_numere[i])
    else:
        numere_negative.append(alte_numere[i])

noua_lista = numere_pozitive + numere_negative          #se va crea o noua lista care are elementele ce erau la inceput in alte_numere

for i in range(0, len(noua_lista)):
    if noua_lista[i] % 2 == 0:
        numere_pare.append(noua_lista[i])
    else:
        numere_impare.append(noua_lista[i])

for i in range(0, len(numere_pozitive)):
    print(f"Numerele pozitive sunt: {numere_pozitive[i]}.")
for i in range(0, len(numere_negative)):
    print(f"Numerele negative sunt: {numere_negative[i]}.")
for i in range(0, len(numere_pare)):
    print(f"Numerele pare sunt: {numere_pare[i]}.")
for i in range(0, len(numere_impare)):
    print(f"Numerele impare sunt: {numere_impare[i]}.")

#12)
adevarata_lista = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(0, len(adevarata_lista)):
    for j in range(i+1, len(adevarata_lista)):
        if adevarata_lista[i] > adevarata_lista[j]:
            adevarata_lista[i], adevarata_lista[j] = adevarata_lista[j], adevarata_lista[i]
print(f"Lista ordonata este: {adevarata_lista}.")

#13)
import random
numar_secret = random.randrange(1, 31)
numar_ghicit = None
while numar_ghicit != numar_secret:
    numar_ghicit = int(input("Introduceti un numar de la 1 la 30: "))
    print(f"Nr. ghicit = {numar_ghicit}.")
    print(f"Nr. secret = {numar_secret}.")
    if numar_ghicit == numar_secret:
        print("Felicitari! Ai ghicit!")
        print("Se va opri ciclul.")
        break
    elif numar_ghicit > numar_secret:
        print("Nr secret e mai mic.")
    else:
        print("Nr secret e mai mare.")

#14)
#piramida
alegere = int(input("Introduceti un numar: "))
for i in range(alegere + 1):
    for j in range(i):
        print(i, end="")
    print("\r")

#15)
#nested for
tastatura_telefon = [ [1, 2, 3],[4, 5, 6],[7, 8, 9],[0] ]
for i in tastatura_telefon:
    for j in i:
        print(j)