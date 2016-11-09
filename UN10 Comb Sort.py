numbers=[]
count=int(input("How many numbers to be sorted?-->"))
switched=1
for a in range (0,count):
    numbers.append(int(input("-->")))
while switched>0:
    switched=0
    for a in range (0,count-1):
        if numbers[a]>numbers[a+1]:
            switched=switched+1
            temp=numbers[a]
            temp2=numbers[a+1]
            numbers.remove(numbers[a])
            numbers.remove(numbers[a])
            numbers.insert(a,temp2)
            numbers.insert(a+1,temp)
            print(numbers)
