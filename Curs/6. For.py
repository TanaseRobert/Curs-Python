# dalmatienii
for i in range(1, 102):
    print(f'Dalmatianul cu numarul {i}')
print('\b')

# dalmatienii din 2 in 2
for i in range(1, 102, 2):
    print(f'Dalmatianul cu numarul {i}')
print('\b')

numere = [3, 7, 10, 20, 30]
# parcurgere lista cu for prin intermediul indexului
for i in range(0, len(numere)):
    print(f'Indexul curent este {i}')
    print(f'Numarul curent este {numere[i]}')
    print('\b')

# for each
s = 0
for numar in numere:
    print(f'Numarul curent este {numar}')
    s += numar
print(f'Suma este {s}')

# de cate ori apare 3 in [3, 2, 3, 5, 8, 3]
lista = [3, 2, 3, 5, 8, 3]
count = 0
for element in lista:
    if element == 3:
        count += 1
print(f'Cifra 3 apare de {count} ori')