n = 5 # Number of processes
m = 3 # Type of devices

# Allocation matrix (deadlock avoidance purposes)(resource allocation)
#         A  B  C
alloc = [[0, 1, 0],  # P0
         [2, 0, 0],  # P1
         [3, 0, 2],  # P2
         [2, 1, 1],  # P3
         [0, 0, 2]]  # P4

# Require each processes to declare MAX number of resources it may need
#needs advance knowledge of maximum needs
#       A  B  C
max = [[7, 5, 3],  # P0
       [3, 2, 2],  # P1
       [9, 0, 2],  # P2
       [2, 2, 2],  # P3
       [4, 3, 3]]  # P4

#        A   B  C
total = [10, 5 ,7]       # total instances of devices A B C
totalAllocation = [0]*m

for i in range(n):
    for j in range(m):
        totalAllocation[j] += alloc[i][j]  # A ,B,C
print("Total Allocation", totalAllocation) # [7,2,5]

#initialized list of available resources for each device
avail = [0]*m
for i in range(m):
    avail[i] = total[i] - totalAllocation[i]  # 10 , 5, 7 - 7 , 2, 5 = [3,3,2] (a-a,b-b,c-c)
print("Available Devices", avail, "\n")

# safe state -> no deadlock
# unsafe state -> possibility of deadlock
# avoidance ensure that a system never enter an unsafe state
# this deadlock avoidance can be explained by using Banker's Algorithm

executedProcess = [0]*n  # list for executed process
processState = [0]*n     # list for process state either 1(executed) or 0(non executed yet)

#initialize 2d array matrix for need. there is calculation to 
need = [[0 for i in range(m)] for i in range(n)]

#this for loop is to count the need resources for each process
for i in range(n):                              # [[7, 4, 3],  max matrix - allocation matrix = need matrix
    for j in range(m):                          #  [1, 2, 2],
        need[i][j] = max[i][j] - alloc[i][j]    #  [6, 0, 0],
                                                #  [2, 1, 1],
                                                #  [5, 3, 1]]

# find process in safe state and assign that first
point = 0
for z in range(5):
    for i in range(n):
        if (processState[i] == 0): # process has not executed yet
            flag = 0
            for j in range(m):
                if (need[i][j] > avail[j]):  # to find whether process in safe state or not
                    flag = 1
                    break
            if (flag == 0):
                executedProcess[point] = i   # contain process number in list
                print("P", executedProcess[point], " is in safe state, ", sep='', end='')
                print(alloc[i], "devices is allocated then were released after P",
                      executedProcess[point], " executed", sep='')
                point += 1
                for w in range(m):
                    avail[w] += alloc[i][w]
                processState[i] = 1
                print("available resources becomes ", avail, "\n")

print("The SAFE sequence: ")
for i in range(n - 1):
    print("P", executedProcess[i], " -->", sep='', end=' ')
print("P", executedProcess[n - 1], sep='', end=' ')