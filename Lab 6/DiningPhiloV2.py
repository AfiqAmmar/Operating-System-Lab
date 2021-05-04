import threading
import random
import time

class Philosopher(threading.Thread):
    running = True  #used to check if everyone is finished eating

    def __init__(self, index, leftFork, rightFork):
        threading.Thread.__init__(self)
        self.index = index
        self.leftFork = leftFork
        self.rightFork = rightFork

    def run(self):
        while(self.running):
            # Philosopher is thinking (but really is sleeping).
            time.sleep(10)
            print ('Philosopher %s is hungry.' % self.index)
            self.dine()

    def dine(self):
        # if both the forks are free, then philosopher will eat
        while self.running:
            self.leftFork.acquire() # wait operation on left fork
            locked = self.rightFork.acquire(True) # we Place true here to get a return value of true to break from loop
            if locked: 
                break 
        self.dining()
        #unlock both forks after eating
        self.rightFork.release()
        self.leftFork.release()
 
    def dining(self):			
        print ('Philosopher %s starts eating. '% self.index)
        time.sleep(10)
        print ('Philosopher %s finishes eating and leaves to think.' % self.index)


diners=5
forks = [threading.Semaphore() for n in range(diners)] #initialising array of semaphore i.e forks
philosophers= [Philosopher(i, forks[i%diners], forks[(i+1)%diners])for i in range(diners)]
Philosopher.running = True
for p in philosophers: 
    p.start()
time.sleep(40)
Philosopher.running = False
print ("Kedai nak tutup!!.")
