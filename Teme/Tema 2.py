#1)
#if else este un bloc de comenzi prin care se intreaba valoarea de adevar a unui propozitii, pe doua ramuri
#prima fiind cu if si a doua (else) fiind inversa primei
#se verifica valoarea de adevar 1 sau 0 pentru prima
#in cazul in care e adevarata se executa setul de comenzi pentru if
#in cazul in care NU e adevarata se trece la urmatoarea(else) si se va executa blocul de comenzi

#2)
x = int(input("Introduceti valoarea pentru x: "))
if x >= 0:
    print(f"{x} este numar natural.")
else:
    print(f'{x} nu este numar natural.')


#3)
if x > 0:
    print(f"{x} este numar pozitiv.")
elif x == 0:
    print(f"{x} este numar neutru.")
else:
    print(f"{x} este numar negativ.")

#4)
if x > -2 and x < 13:
    print(f"{x} apartine intervalului (-2,13).")
else:
    print(f"{x} nu apartine intervalului (-2,13).")

#5)
y = int(input("Introduceti valoarea pentru y: "))
u = x - y
if u < 5:
    print(f"Diferenta dintre {x} si {y} este mai mica de 5")
else:
    print("Eroare")

#6)
if x < 5 or x > 27:
    print(f"{x} nu apartine intervalului cerut.")
else:
    print(f"{x} apartine intervalului cerut.")

#7)
v = max(x,y)
if x == y:
    print(f"{x} si {y} sunt egale.")
else:
    print(f"Mai mare este {v}.")

#8)
z = int(input("Introduceti valoarea pentru z: "))
if x == y and y == z:
    print("Triunghi echilateral")
elif (x == y or x == z) and y !=z:
    print("Triunghi isoscel")
else:
    print("Triunghi oarecare")

#9)
w = input("Introduceti o litera: ")
if w == 'A' or w == 'E' or w == 'I' or w == 'O' or w == 'U' or w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u':
    print("Vocala")
else:
    print("Consoana")

#10)
r = float(input("Introduceti o nota: "))
if r > 9:
    print("Calificativ A.")
elif r > 8 and r <= 9:
    print("Calificativ B.")
elif r > 7 and r <= 8:
    print("Calificativ C.")
elif r > 6 and r <= 7:
    print("Calificativ D.")
elif r > 5 and r <= 6:
    print("Calificativ E.")
else:
    print("Calificativ F.")

#11)
if x >= 1000:
    print(f'{x} are minim 4 cifre.')
else:
    print(f'{x} nu are minim 4 cifre.')

#12)
if x >= 100000 and x <=999999:
    print(f'{x} are exact 6 cifre.')
else:
    print(f'{x} are exact 6 cifre.')

#13)
if x % 2 == 0:
    print(f'{x} este numar par.')
else:
    print(f'{x} este numar impar.')

#14)
maxim = 0
if x > y:
    if z > x:
        maxim = z
    else:
        maxim = x
else:
    if z > y:
        maxim = z
    else:
        maxim = y
print(f"Maximul dintre cele trei numere este: {maxim}.")

#15)
if x < (y + z) and y < (x + z) and z < (x + y) and x > 0 and y > 0 and z > 0 and x + y + z == 180:
    print("Putem avea triunghi cu aceste unghiuri.")
else:
    print("Nu putem avea triunghi cu aceste unghiuri.")

#16)
sir = "Coral is either the stupidest animal or the smartest rock"
s = int(input("Alegeti un numar intreg: "))
print(sir[0 : len(sir)-s])

#17)
altsir = sir[0:5] + sir[len(sir)-5 : len(sir)]
print(altsir)

#18)
t = sir.find("rock")
print(t)
print(sir[0:t])

#19, 20)
sir19 = input("Introduceti un sir: ")
if sir19 == sir19[::-1]:
    print("Primul si ultimul caracter al lui sir19 sunt egale.")
else:
    print("Primul si ultimul caracter al lui sir19 NU sunt egale.")

#21)
varsta = int(input("Introduceti varsta: "))
pasaport = input("Aveti pasaport? (se va raspunde cu DA sau NU: ")
mama = input("Sunteti cu mama dvs? (se va raspunde cu DA sau NU: ")
tata = input("Sunteti cu tatal dvs? (se va raspunde cu DA sau NU: ")
actmama = input("Aveti procura de la mama dvs? (se va raspunde cu DA sau NU: ")
acttata = input("Aveti procura de la tatal dvs? (se va raspunde cu DA sau NU: ")

if varsta >= 18 and pasaport == "DA":
    print("Ma pot imbarca")
elif varsta < 18 and pasaport == "DA" and mama == "DA" and tata == "DA":
    print("Ma pot imbarca")
elif (pasaport == "DA" and mama == "DA" and acttata == "DA") or (pasaport == "DA" and tata == "DA" and actmama == "DA"):
    print("Ma pot imbarca")
else:
    print("Nu ma pot imbarca")

#22)
import random
dice_roll = random.randrange(1, 7)                            #se va genera un numar intreg de 1 la 6
ghici = int(input("Ce iti arata zarul? 1,2,3,4,5 sau 6? "))
if dice_roll == ghici:
    print(f"Ai ghicit. Felicitari! Ai ales {ghici} si zarul a fost {dice_roll}.")
else:
    if ghici > dice_roll:
        print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {ghici} dar a fost {dice_roll}.")
    else:
        print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {ghici} dar a fost {dice_roll}.")