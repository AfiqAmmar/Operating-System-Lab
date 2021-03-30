reference = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 1, 2, 0]
pageFrame = 4
temp = []

def lruPlacement(x):
    block = []
    for n in range(x-1, -1, -1):
        current = reference[n] in block
        if len(block)<=pageFrame and not current:
            block.append(reference[n])
    else:
        for i in range(len(temp)):
            if temp[i] == block[pageFrame-1]:
                temp[i] = reference[x]
                break
        print(temp)

count = 0
for x in range(len(reference)):
    exists = reference[x] in temp
    if exists:
        print(temp, "hit", reference[x])
        count += 1
    else:
        if len(temp)<pageFrame:
            temp.append(reference[x])
            print(temp)
        else:
            lruPlacement(x)

print("Number of hit count is :", count)
pageFault = len(reference)-count
print("Number of page fault: ", pageFault)
print("Success Rate: ", (count/len(reference))*100, "%")