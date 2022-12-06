fructe = ['mar', 'portocale', 'pepene', 'mango', 'cirese', 45, True]

# afisare lista
print(fructe)

# accesare un element in functie de index
print(fructe[1])

# adaugare un nou element
fructe.append('23')

# suprascriere un element
fructe[2] = 'harbuz'

# afisare noua lista
print(fructe)

# aflare dimensiunea listei
print(len(fructe))

# scoatere si returnare ultimul element
last = fructe.pop()
print('Ultimul element:', last)
print('Noua lista:', fructe)

# numarul de aparitii al unui element
print(fructe.count('mango'))

fructe_exotice = ['kiwi', 'ananas']

# concatenare de liste
fructe.extend(fructe_exotice)
print(fructe)