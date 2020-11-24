#elements idnexed, and also are inmutable



handler = open('mbox-short.txt')


horas = dict()
for line in handler:

    if line.startswith('From:'): continue

    if not line.startswith('From'): continue

    temp = line.split()

    hour = temp[5].split(":")



    horas[hour[0]] = horas.get(hour[0], 0) + 1

for h,c in sorted(horas.items(),reverse=False):

    print(h,c)







