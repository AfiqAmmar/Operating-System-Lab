ReadyQueue= {1:7,2:5,3:6,4:7}#to show readyqueue popping
ReadyQueueRem= {1:7,2:5,3:6,4:7}#static readyqueue
WaitingTime={}
TurnAroundTime={}
time=0
quantumTime=7541

while len(ReadyQueue)>0:
    iterator=list(ReadyQueue.keys())[0]#to get first key of the dictionary
     
    print("time "+str(time))
    print("job "+str(iterator)+":"+str(ReadyQueue[iterator]))
    print(ReadyQueue)
    
    if ReadyQueue[iterator] > quantumTime:
        print("moving to back of queue")
        newValue=ReadyQueue[iterator]-quantumTime
        ReadyQueue.pop(iterator)
        ReadyQueue[iterator]=newValue
        time+=quantumTime
        
    else:
        print("popping")
        job=list(ReadyQueue.keys())[0]
        time+=ReadyQueue[job]
        WaitingTime[job]=time - ReadyQueueRem[job]
        ReadyQueue.pop(iterator)

    
    print(ReadyQueue)
    print("\n")

for i in ReadyQueueRem.keys():
    TurnAroundTime[i]=(WaitingTime[i] - ReadyQueueRem[i])

print("turn around time: "+str(TurnAroundTime))
print("jobs' waiting times: "+ str(WaitingTime))

print("Processes    Burst Time     Waiting", "Time    Turn-Around Time")
for i in ReadyQueueRem.keys():
        print(" ", i , "\t\t", ReadyQueueRem[i], "\t\t", WaitingTime[i], "\t\t", TurnAroundTime[i])


    