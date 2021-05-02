import random

chopsticks=[1]*5
philosophers=[0]*5

JobCompleted=0
while(JobCompleted!=5):
    hungry=[0]*5
    for philosopher in range(len(philosophers)):
        hungry=random.randint(0,2)
        philosophers[philosopher]=hungry
        if philosophers[philosopher]==1:
            print("Philosohper "+str(philosopher)+" is hungry")
            if chopsticks[philosopher]==1 and chopsticks[(philosopher+1)%5]==1:
                chopsticks[philosopher]=0
                chopsticks[(philosopher+1)%5]=0
                JobCompleted+=1
                print("Philosohper "+str(philosopher)+" able to eat")
            else:
                print("Philosohper "+str(philosopher)+" cant eat cause chopstick "+str(chopsticks[philosopher])+ " or "+str(chopsticks[(philosopher+1)%5]))
        else:
            print("Philosohper "+str(philosopher)+" aint hungry")
            continue 
        print(str(chopsticks))
            
            
                 
    