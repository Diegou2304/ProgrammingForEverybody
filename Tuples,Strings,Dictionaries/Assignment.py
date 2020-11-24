import re

handler = open('actualdata.txt')

#Extract all the numbers in the file and compute the sum of the numbers

suma =float()
for line in handler:

    stuff = re.findall('[0-9]+',line)

    if len(stuff) == 0: continue

    for number in stuff:

        print(number)

        suma = suma + int(number)


print(int(suma))