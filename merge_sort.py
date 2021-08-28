import time

def meregesort( data, drawData, timetTick):
    mergesort_alg(data, 0,len(data)-1,drawData, timetTick)



def mergesort_alg(data, left, right, drawData, timeTick):
    if left < right :
        middle = (left + right) // 2
        mergesort_alg(data, left, middle, drawData, timeTick)
        mergesort_alg(data, middle+1, right,drawData, timeTick )
        merge(data, left, middle, right, drawData, timeTick)

def merge(data, left ,middle, right, drawData, timeTick):
    drawData(data, getcolorArray(len(data), left, middle,right))
    time.sleep(timeTick)

    leftpart = data[left:middle+1]
    rightpart = data[middle+1:right+1]

    leftind = rightind = 0

    for dataindx in range(left, right+1):
        if leftind < len(leftpart) and rightind < len(rightpart):
            if leftpart[leftind] <= rightpart[rightind]:
                data[dataindx]=leftpart[leftind]
                leftind = leftind+1
            else:
                data[dataindx]=rightpart[rightind]
                rightind= rightind+1
        elif leftind <len(leftpart):
            data[dataindx] = leftpart[leftind]
            leftind= leftind+1
        else:
            data[dataindx] = rightpart[rightind]
            rightind = rightind+1

    drawData(data, ['green' if x >=left and x <= right else 'white' for x in range(len(data))])
    time.sleep(timeTick)

def getcolorArray(leght, left, middle, right):
    
    colorArray = []

    for i in range (leght):
        if i>=left and i<=right:
            if i>=left and i<=middle:
                colorArray.append('yellow')
            else:
                colorArray.append('blue')
        else:
            colorArray.append('white')

    return colorArray