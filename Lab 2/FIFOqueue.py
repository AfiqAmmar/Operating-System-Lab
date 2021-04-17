class Queue:
    def __init__ (self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insertQueue(self,item):
        self.items.insert(0,item)

    def popQueue (self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printQueue(self):
        for items in self.items:
            print(items," | ",end='')

q = Queue()
pageFrame = 3
reference = [3,7,12,2,8,9,12]
success = 0
interupt = 0

for i in range (0,len(reference)):
    if(q.size()<pageFrame):
        q.insertQueue(reference[i])
        success +=1
    else:
        interupt +=1
        print("Interrupt:",interupt)
        print()
        q.popQueue()
        q.insertQueue(reference[i])

    print("time :",i,end=" ")
    print("Reference: ",reference[i])
    q.printQueue()
    print()
    print()

successrate = success/len(reference)*100
fail = 100 - successrate
print("Success rate is:",round(successrate,2),"%")
print("Failure rate is:",round(fail,2),"%")
print("Interupt:",interupt)




