import time

def insertionSort(data,drawData, timeTick):
    
    for i in range(1,len(data)):
        val = data[i]
        hole = i
        drawData(data,['green' if x <= hole else 'white' for x in range(len(data))])
        time.sleep(timeTick)
        while hole>0 and data[hole-1] > val:
            data[hole] = data[hole-1]
            hole = hole-1
        data[hole] = val
        drawData(data,['green' if x <= hole else 'white' for x in range(len(data))])
        time.sleep(timeTick)
