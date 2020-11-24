import re

x =  "hola esta es la prueba nro 10, porque ohy 12 de septiembre celebramos la vuelta"
y = re.findall('[0-9]+',x)

print (y)

z = "YOLA quiero"

y = re.findall('[AEIOU]+',z)

print(y)

a = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"

y = re.findall('\S+@\S+',a)
print(y)

y = re.findall('^From (\S+@\S+) ',a)
print(y)

y = re.findall('@( [^ ]*)',a)
print(y)


hand = open('mbox-short.txt')

numlist = list()

for line in hand:


    #Get the numbers that Finds XDs
    line = line.rstrip()

    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)

    if len(stuff) !=1: continue

    num = float(stuff[0])
    numlist.append(num)
print('Maximum:',max(numlist))




