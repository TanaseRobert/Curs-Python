# Input de la tastatura
numar = int(input('Introduceti un numar: '))

if numar % 2 == 0:
    print(f'Numarul {numar} este par.')
else:
    print(f'Numarul {numar} este impar.')

if numar > 0:
    print(f'Numarul {numar} este pozitiv.')
elif numar == 0:
    print(f'Numarul {numar} este nul.')
else:
    print(f'Numarul {numar} este negativ.')