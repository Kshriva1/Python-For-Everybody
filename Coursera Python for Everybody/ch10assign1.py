name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time = dict()
for line in handle:
    if line.startswith('From '):
        lst = line.split()
        llst = lst[5].split(':')
        time[llst[0]] = time.get(llst[0],0) + 1

for k,v in sorted(time.items()) :
    print(k,v)

x = time.items()
print(x)    
