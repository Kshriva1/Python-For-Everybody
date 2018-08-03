fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    slst = list()
    slst = line.split()
    for num in range(len(slst)) :
        if slst[num] not in lst :
            lst.append(slst[num])
lst.sort()
print(lst)
