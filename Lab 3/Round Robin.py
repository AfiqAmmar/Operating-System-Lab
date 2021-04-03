ReadyQueue= {1:2,2:5,3:6,4:7}

quantumTime=2
time=0
iterator=1 #is the key
queueLength=len(ReadyQueue)
starting=0

while len(ReadyQueue)>0:
    print("time "+str(time))
    iterator=list(ReadyQueue.keys())[0]#to get first key of the dictionary
    print("key "+str(iterator))
    print("job "+str(iterator)+":"+str(ReadyQueue[iterator]))
    
    print(ReadyQueue)
    
    if ReadyQueue[iterator] == 2 or ReadyQueue[iterator] < quantumTime:
        print("popping")
        ReadyQueue.pop(iterator)
    else:
        print("moving to back of queue")
        newValue=ReadyQueue[iterator]-quantumTime
        ReadyQueue.pop(iterator)
        ReadyQueue[iterator]=newValue
 
    time+=1
    print(ReadyQueue)
    print("\n")
    