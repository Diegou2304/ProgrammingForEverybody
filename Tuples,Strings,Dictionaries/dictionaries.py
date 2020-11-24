# Most powerfull collection

purse = dict()

purse['money'] = 23
purse['candy'] = 3

# Unpredictible order


# counting with dictionaries

# Default value if it does not find the value or the key
purse.get('money', 0)
print(purse.values())

handler = open('mbox-short.txt')

emails = dict()
for line in handler:

    if line.startswith('From:') : continue
    if line.startswith('From'):
        temp = line.split()
        

        emails[temp[1]] = emails.get(temp[1], 0) + 1



correo_mayor = ''
numero_mayor = 0
for key, value in emails.items():

    if correo_mayor == '' and numero_mayor == 0:
        correo_mayor = key
        numero_mayor = value
        continue

    if numero_mayor < value:
        correo_mayor = key
        numero_mayor = value

print(correo_mayor, numero_mayor)
