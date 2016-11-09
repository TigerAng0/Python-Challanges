numbers=[]
sortnums=[]
count=int(input("How many numbers to be sorted?-->"))
for a in range (0,count):
    numbers.append(int(input("-->")))
for a in range(0,count):
    smallest=99999999
    for b in range(0,count-a):
        if numbers[b]<smallest:
            smallest=numbers[b]
    sortnums.append(smallest)
    numbers.remove(smallest)
    print(sortnums)
