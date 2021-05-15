filelength = 10
files = [0]*filelength
for x in range(files.__len__()):
    files[x] = 0

flag = 1

while flag == 1:
    start = int(input("Please enter the starting block:"))
    while (start<=0 or start>filelength):
        if start<=0:
            print("Please enter a positive number!")
        if start>50:
            print("Starting block entered exceeds files limit!")
        start = int(input("Please enter the starting block:"))

    length = int(input("Please enter the length of the files:"))
    while length<=0 or length>filelength:
        if length<=0:
            print("Please enter a positive number!")
        if length>50:
            print("Starting block entered exceeds files limit!")
        length = int(input("Please enter the length of the files:"))

    check = 0
    for x in range(length):
        if files[start+x] == 0:
            check +=1
    
    if check == length:
        for x in range(length):
            files[start+x] = 1
        print("Files are allocated")  
    else:
        print("Files are not allocated")

    choice = True
    while True:
        resume = input(("Do you want to enter more files? (yes/no)"))
        if resume == 'yes' or resume.upper() == 'YES':
            flag = 1
            break
        elif resume == 'no' or resume == 'NO':
            flag = 0
            break
        else:
            choice = True

print("Files allocated:")
for x in range(files.__len__()):
            print("     Files [",x+1,"]           allocated")

