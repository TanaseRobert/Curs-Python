#1)
note_muzicale = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
#a)
print(note_muzicale)                              #lista
#b)
note_muzicale == note_muzicale.reverse()          #suprascriere
#c)
print(note_muzicale)                              #lista care a fost ordonata invers
#d) si e)
print(note_muzicale[::-1])                        #lista ordonata invers a fost iarasi inversata, rezultand lista initiala

#2)
print(note_muzicale.count("do"))                  #numarul de aparitii pentru "do" ---> 2

#3)
#metoda 1
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
list3 = list1 + list2                             #concatenare de liste
print(list3)
#metoda 2
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
for x in list2:
    list1.append(x)                               #se adauga toate elementele din list2 la capatul lui list 1
print(list1)
#metoda 3
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
list1.extend(list2)                               #se extinde lista 1 la final cu toata lista 2
print(list1)


#4)
list3.sort()                                      #se va sorta crescator lista
print(list3)
list3.remove(0)                                   #se va elimina elementul 0 din lista
print(list3)

#5)
list3 = list1 + list2                             #suprascriem lista 3 ca suma celor doua de la ex3)
if len(list3) > 0:
    print("Lista nu este goala.")
else:
    print("Lista este goala.")

#6)
list3.clear()                                     #se vor sterge sterge toate elementele listei3

#7)
if len(list3) == 0:                               #conditie adevarata in urma comenzii de la 6)
    print("Lista este goala.")
else:
    print("Lista nu este goala.")

#8)
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())                              #se vor afisa cheile(Ana, Gigel, Dorel)

#9)
print(f"Ana a luat nota {(dict1.get('Ana'))}.")
print(f"Gigel a luat nota {(dict1.get('Gigel'))}.")
print(f"Dorel a luat nota {(dict1.get('Dorel'))}.")

#10)
dict1["Dorel"] = 6                              #o prima metoda
dict1.update({"Dorel": 6})                      #o a doua metoda
print(f"Dorel a facut contestatie si a scos o nota de {(dict1.get('Dorel'))}.")

#11)
dict1.pop("Gigel")                              #se va sterge cheia Gigel
dict1["Ionica"] = "9"                           #se va adauga cheia Ionica si i se va atribui valoarea 9
print(dict1)                                    #se va printa noul dictionar
print(dict1.keys())                             #se vor afisa cheile(Ana, Dorel, Ionica)

#12)
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')                           #se adauga un nou element
print(zile_sapt)

#13)
zzz = zile_sapt.issuperset(weekend)
print(zzz)
if zzz == True:
    print("Weekend este un subset al zilelor din sapt.")
else:
    print("Weekend NU este un subset al zilelor din sapt.")


#14)
#metoda I
#zile_sapt.symmetric_difference_update(weekend) #diferenta celor doua seturi
#print(zile_sapt)                               #se va afisa luni, marti, miercuri, joi si vineri (in orice ordine)
#metoda a II-a
#z = zile_sapt.symmetric_difference(weekend)    #diferenta celor doua seturi ( cu un nou set )
#print(z)                                       #se va afisa luni, marti, miercuri, joi si vineri (in orice ordine)

#15)
#metoda I
#zile_sapt.intersection_update(weekend)         #intersectia celor doua seturi
#print(zile_sapt)                               #se va afisa sambata si duminica
#metoda a II-a
#zz = zile_sapt.intersection(weekend)           #intersectia celor doua seturi ( cu un nou set )
#print(zz)                                      #se va afisa sambata si duminica

#16)
echipa = ["rusescu", "tanase", "chipciu", "popa", "nikolic"]
rezerve = ["rocha", "mihai costea", "florin costea", "tatu", "iancu"]
schimbari_max = 3
jucator_out = input("Introdeti numele jucatorului pe care vreti sa il scoateti de pe teren: ")
if jucator_out in echipa and schimbari_max > 0:
    echipa.remove(jucator_out)
    jucator_in = input("Introdeti numele jucatorului pe care vreti sa il bagati pe teren: ")
    if jucator_in in rezerve:
        echipa.append(jucator_in)
        print(f"A intrat {jucator_in} si a iesit {jucator_out}.")
        print(echipa)
        schimbari_max -= 1
    else:
        print(f"Jucatorul {jucator_in} nu este pe banca de rezerve.")
else:
    print(f"Nu se poate efectua schimbarea deoarece jucatorul {jucator_out} nu e in teren.")
    print(f"Mai aveti {schimbari_max} schimbari.")
