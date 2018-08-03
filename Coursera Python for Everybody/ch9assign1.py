name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
words = dict()
for line in handle :
    if line.startswith('From '):
        lst = line.split()
        words[lst[1]] = words.get(lst[1],0) + 1


bigcount = 0
bigword = 0

for k,v in words.items():
    if v is None or v > bigcount:
        bigcount = v
        bigword = k

print(bigword,bigcount)
