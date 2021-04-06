ReadyQueue= {1:7,2:5,3:6,4:7}
ReadyQueueRem= {1:7,2:5,3:6,4:7}
WaitingTime={}
TurnAroundTime={}
time=0
quantumTime=2

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

print("jobs' waiting times: "+ str(WaitingTime))

for i in range(1,len(ReadyQueueRem)+1):
    TurnAroundTime[i]=(WaitingTime[i] - ReadyQueueRem[i])
print("turn around time: "+str(TurnAroundTime))

    