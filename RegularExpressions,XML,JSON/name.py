#Variables
#letter or underscore

#MMemonic

#chosse a variable name that is consistent and makes sense



#Files

#the function open to prepare the file


#handle = open(filename,mode)

#Gives all the characteristics print(handle)

#file_input()

#Read files

#It prints each line of code
#for x in file:

 #   print(x)

# file.read() it reads all the stuff without the \n

file_name = input("Enter File Name:")

file_handler = open(file_name)

acum = 0
lines = 0
for line in file_handler:

    if not line.startswith('X-DSPAM-Confidence:'): continue

    temp_value = line[line.find('.')-1:]
    lines += 1
    acum = float(temp_value) + acum

 #   print((line.upper()).rstrip())

print("Average spam confidence:",acum/lines)



















