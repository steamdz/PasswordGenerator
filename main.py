import random

#Var
LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS ="0123456789"
SYMBOLS ="{}[]()?!@#&^%"

#VarALL
ALL = LOWER+UPPER+NUMBERS+SYMBOLS
LENGTH = 16

#Affichage
PASSWORD = "".join(random.sample(ALL,LENGTH))
print(PASSWORD)



