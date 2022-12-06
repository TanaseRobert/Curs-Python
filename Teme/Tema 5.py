#1)
def suma(a,b):
    return a + b
print(suma(3, 4))                                        #se va afisa 7
print(suma(-3, 45))                                      #se va afisa 42

#2)
def paritate(c):
    if c % 2 == 0:
        return True
    else:
        return False
print(paritate(-35))                                     #se va afisa False
print(paritate(86))                                      #se va afisa True

#3)
nume = input("Introduceti numele dumneavoastra complet: ")
def nr_caractere(nume):
    nr = 0
    for i in range(0, len(nume)):
        if nume[i] != ' ':                               #se vor elimina din start spatiile din sir2
            nr = nr + 1
    return nr
print(nr_caractere(nume))

#4)
def arie_dreptunghi(lungime, latime):
    return lungime * latime
print(arie_dreptunghi(20 , 30))                          #se va afisa 600
print(arie_dreptunghi(2, 4))                             #se va afisa 8

#5)
def arie_cerc(raza):
    pi = 3.14
    return pi * (raza  ** 2)
print(arie_cerc(5))                                      #se va afisa 78.5
print(arie_cerc(9))                                      #se va afisa 254.34

#6)
sir = input("Introduceti un sir: ")
def a_fi_sau_a_nu_fi(sir):
    d = input("Introduceti un caracter pentru a vedea daca se afla in sirul initial: ")
    e = sir.find(d)                                      #se va cauta indexul lui 'd' in sir
    if e >= 0:                                           #caracterul 'e' este gasit in sir
        return True
    else:                                                #caracterul 'e' nu este gasit in sir
        return False
print(a_fi_sau_a_nu_fi(sir))

#7)
sir2 = input("Introduceti un sir pentru a vedea numarul de caractere cu si fara majuscule: ")
def majuscule(sir2):
    x = 0
    y = 0
    for i in range(0, len(sir2)):
        if sir2[i] != " ":                               #se vor elimina din start spatiile din sir2
            if sir2[i].islower() == True:                #caracter mic
                x += 1
            else:                                        #majuscula
                y += 1
    print(f"Sirul ales are {x} caractere mici.")
    print(f"Sirul ales are {y} caractere mari.")
majuscule(sir2)

#8)
numere = [3, 5, 9, -4, -7]
def noualista(lista_numere):
    numere2 = []                                        #se va crea o noua lista noua, goala
    for numar in lista_numere:                          #for each
        if numar >= 0:
            numere2.append(numar)                       #conditie pentru a popula noua lista doar cu elemente pozitive
    print(f"Lista initiala doar cu elemente pozitive este: {numere2}.")
noualista(numere)                                       #se va afisa [3, 5, 9]

#9)
e = int(input("Introduceti un numar: "))
f = int(input("Introduceti un alt numar: "))
def mai_mare(e, f):
    if e > f:
        print(f"Primul numar {e} este mai mare decat al doilea numar {f}.")
    elif e < f:
        print(f"Al doilea numar {f} este mai mare decat primul numar {e}.")
    else:
        print(f"Numerele sunt egale.")
mai_mare(e, f)

#10)
g = input("Introduceti un fruct pentru a putea fi adaugat in set: ")
set = {"apple", "banana", "cherry"}
def primeste(g, set):
    if g in set:
        return "Nu am adaugat numarul in set. Acesta exista deja."
        return False
    else:
        set.add(g)                                       #se va adauga elementul g in set
        return True
print(primeste(g, set))                                  #se va afisa False daca g este apple/banana/cherry
                                                         #se va afisa True daca g este orice alt string

#11)
luna = input("Introduceti o luna: ")
def calendar(luna):
    if luna == "Ianuarie" or luna == "Martie" or luna == "Mai" or luna == "Iulie" or luna == "August" or luna == "Octombrie" or luna == "Decembrie":
        return 31
    elif luna == "Aprilie" or luna == "Iunie" or luna == "Septembrie" or luna == "Noiembrie":
        return 30
    elif luna == "Februarie":
        return 28
    else:
        return "Ati introdus un alt format."
print(calendar(luna))

#12)
j = int(input("Introduceti un numar intreg: "))
k = int(input("Introduceti un numar intreg: "))
m = 0
n = 0
o = 0
p = 0
def calculator(j, k):
    m = j + k
    n = j - k
    o = j * k
    p = j / k
    print(f"Suma: {m}")
    print(f"Diferenta: {n}")
    print(f"Inmultirea: {o}")
    print(f"Impartirea: {p}")
calculator(j, k)

#13)
lista_cifre = [1, 3, 1, 5, 9, 7, 7, 5, 5]
def numarare(lista_cifre):
    frecventa = {}
    for cifre in lista_cifre:
        frecventa[cifre] = lista_cifre.count(cifre)
    for key, value in frecventa.items():
        print("% d : % d" % (key, value))
numarare(lista_cifre)

#14)
q = int(input("Introduceti un numar: "))
r = int(input("Introduceti un numar: "))
s = int(input("Introduceti un numar: "))
def maxim(q, r, s):
    maxx = 0
    if q > r:
        if s > q:
            maxx = s
        else:
            maxx = q

    else:
        if s > r:
            maxx = s
        else:
            maxx = r
    return maxx
print(f"Maximul dintre {q}, {r} si {s} este: {maxim(q, r, s)}")

#15)
t = int(input("Introduceti un numar pentru a putea calcula suma: "))
def suma_numerelor(t):
    sum = 0
    i = 0
    while i <= t:
        sum += i
        i += 1
    return sum
print(suma_numerelor(t))

#16)
#metoda I ---> cu un common list
list1 = [3, 1, 6, 4, 9, 13]
list2 = [2, 7, 13, 8, 4, 12]
def la_comun(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3
print(la_comun(list1, list2))

#metoda a II-a ---> cu intersectie
def intersectia(list1, list2):
    return set(list1).intersection(list2)
print(intersectia(list1, list2))

#17)
pret_initial = int(input("Introduceti pretul produsului: "))
reducere = int(input("Introduceti procentajul discount-ului (x%): "))
def black_friday(pret_initial, reducere):
    if reducere <= 100:
        pret_final = (100 - reducere) * pret_initial / 100
        print(f"Pretul final dupa reducere este de: {pret_final}")
    else:
        print("Reducerea dvs. este invalida.")
black_friday(pret_initial, reducere)

#18)
#ora Romaniei
import datetime
tara = "Romania"
def ora_romaniei(tara):
    ora_curenta = datetime.datetime.now()
    return ora_curenta
print(ora_romaniei(tara))

#19)
def get_user_birthday():
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))
    birthday = datetime.datetime(year,month,day)
    return birthday

def calculate_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    delta = date2 - date1
    return delta

bd = get_user_birthday()
now = datetime.datetime.now()
w = calculate_dates(bd,now)
print(w)