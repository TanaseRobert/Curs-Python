# declaram si initializam un map
note = {'Ianis': 10, 'Vlad': 8, 'Gabi': 9}

# adaugam elemente
note['Ovidiu'] = 7

# printam dictul
print(note)

# aflam o nota
print(note['Gabi'])
print(note['Ianis'])

# actualizam valori
note['Vlad'] = 6
print(note)

# aflam dimensiunea
print(len(note))

# sterg valori
note.pop('Ianis')
print(note)

# returneaza doar cheile
print(note.keys())

# returneaza doar valorile
print(note.values())