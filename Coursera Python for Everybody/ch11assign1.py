import re
file = input('Enter the file name: ')
han = open(file)
total = 0
for line in han:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    for i in stuff:
        num = int(i)
        total = total+num
print(total)        
