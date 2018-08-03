largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
        inum = int(num)
    except :
        print("Invalid input")
        continue
    if smallest is None :
        smallest = inum
        largest = inum
        continue
    elif inum  < smallest:
        smallest = inum
        continue
    elif inum > largest:
        largest = inum
        continue


print("Maximum", "is", largest)
print("Minimum","is",smallest)

	
