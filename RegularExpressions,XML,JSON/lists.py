file_name = 'romeo.txt'

handler = open(file_name)

words = []
for line in handler:

    temp = line.split()



    for value in temp:

        if value not in words:
            words.append(value)

#Index for position

print(sorted(words))


handler_2 = open('mbox-short.txt')


counter = 0
for line in handler_2:




    if  not line.startswith('From'): continue

    if line.startswith('From:') : continue

    counter += 1

    temp_line = line.split()

    print(temp_line[1])

print("There were",counter,"lines in the file with From as the first words")