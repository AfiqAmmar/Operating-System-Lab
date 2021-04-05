def process(queue):
    queue.sort(key = lambda x: x[1])  #To sort queue based on cpu cycles
    #print("Sorted cpu cycles:", queue)

def waittime(queue):
    
    waittable = [0] #Create a table to hold the waiting time with 0 as the first value
    wait = ([bt[1] for bt in queue]) #Extract only the second element from the sorted queue to get the burst time
    processwait = ([pt[0] for pt in queue]) #Extract only the first element from the sorted queue to get the process number
    for i in[wait]: #To add sorted burst table to waittable
        waittable +=i

    tat = ([bt[1] for bt in queue]) #Create a table to hold the turnaround time

    #print(waittable)
    #print(processwait)
    totalwait = 0 #Define all the variables needed
    i = 0
    waitavg = 0
    totaltat = 0
    tatavg = 0

    for j in range(len(waittable)-1):
        totalwait = totalwait + waittable[j] #To iterate the waiting value eg: [0]+[0+1]+[0+1+n]...
        totaltat = totaltat + tat[j] #To iterate the turnaround value eg: [0]+[0+1]+[0+1+n]...
        print("Process", processwait[i], "Waiting time", totalwait, "Turnaround time", totaltat)
        i = i + 1
        waitavg += totalwait #Sum of waiting time
        tatavg += totaltat #Sum of turnaround time

    print("Average waiting time is", waitavg/len(tat), "\nAverage turnaround time is", tatavg/len(tat))

queue = [[1,6], [2,3], [3,4], [4,9]]
process(queue)
waittime(queue)





