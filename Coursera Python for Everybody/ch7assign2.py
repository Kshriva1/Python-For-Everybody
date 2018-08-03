# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count+1
    pos = line.find('.')
    fline = line[pos-1:]
    ffline = float(fline)
    sum = sum + ffline
print("Average spam confidence:",sum/count)
