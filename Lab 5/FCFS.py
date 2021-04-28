def FCFS(request, currentPosition):
    seekTime = 0 # initalize seek time
    
    for i in range(0, len(request)):
        # head is set to currentPosition
        #increment seek time by with the absolute distance of the track from the head.
        seekTime = seekTime + abs(request[i] - currentPosition) 
        print("Current Position:", currentPosition, "Request:", request[i], "Seek Time:", seekTime)
        currentPosition = request[i] # set head to track

    print("Total Seek Time: ", seekTime)

request = [176, 79, 34, 60, 92, 11, 41, 114] # initalize tracks
currentPosition = 48 # initalize current position (position of the disk head)
FCFS(request, currentPosition)