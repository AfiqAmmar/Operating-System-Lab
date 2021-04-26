def FCFS(request, currentPosition):
    seekTime = 0
    
    for i in range(0, len(request)):
        seekTime = seekTime + abs(request[i] - currentPosition)
        print("Current Position:", currentPosition, "Request:", request[i], "Seek Time:", seekTime)
        currentPosition = request[i]

    print("Total Seek Time: ", seekTime)

request = [176, 79, 34, 60, 92, 11, 41, 114]
currentPosition = 48
FCFS(request, currentPosition)