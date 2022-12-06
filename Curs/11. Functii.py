def PrintGreeting():
    print("Buna ziua! Bine ati venit!")

def PrintGreetingByName(nume, prenume):
    print(f"Buna ziua {nume} {prenume}!")

def MediaNumerelor(a, b, c):
    return (a + b + c) / 3

def piValue():
    return 3.14

def VerificareMajor(varsta):
    if varsta >= 18:
        return True
    elif varsta < 0:
        return "Eroare"
    else:
        return False

age = int(input("Introduceti varsta dvs: "))
if VerificareMajor(age):
    print("Cont creat. Bine ati venit pe aplicatie")
else:
    print("Nu aveti varsta necesara")

# zona de apelare (desktop)
PrintGreeting()
PrintGreetingByName('Ianis', 'Hagi')
print(MediaNumerelor(10, 20, 30))
print(piValue())
print(VerificareMajor(19))
print(VerificareMajor(-1))
print(VerificareMajor(13))

# return-ul este ultima instructiune dintr-o functie, practic programul se va inchide dupa return

# oop
# variabile => atribute / proprietati / fields
# functii => metode