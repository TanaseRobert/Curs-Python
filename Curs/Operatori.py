'''
Operatori:
-> aritmetici: +, -, *, /, %
-> de comparare: <>, ==, !=, <=, >=
-> logici: and, or, !
'''

a = 4
b = 5
print(a % b)                                 # 4
print(a != b)                                # True
print(a % b == 4 and a * b == 25)            # True and False -> False
print(a / b == 0.8 or a > b)                 # True or False -> True