import numpy as np

f1 = []
f2 = []
flagA = 0
flagB = 0
time = 0

x = list(map(int, input("Enter multiple value: ").split()))
list1 = x
arr1 = np.array(list1)
print("Time", time, "Page Frame A", f1, "Page Frame B", f2)

for i in range(0, len(arr1)):
    if f1 == []:
        f1.append(arr1[i])
        flagA += 1

    elif f2 == []:
        f2.append((arr1[i]))
        flagA += 1
        flagB += 1

    else:
        flagA += 1
        flagB += 1

        if flagA > flagB:
            f1.pop()
            flagA = 0
            f1.append(arr1[i])

        else:
            f2.pop()
            flagB = 0
            f2.append(arr1[i])
    time += 1

    print("Time", time, "Page Frame A", f1, "Page Frame B", f2)