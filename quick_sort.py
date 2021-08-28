import time

def partition(data,head,tail,drawData,timeTick):
    border=head
    pivot=data[tail]

    for j in range(head,tail):
        if data[j] < pivot:
            data[j],data[border]=data[border],data[j]
            drawData(data,getcolorArray(len(data), head, tail,border,j,True))
            time.sleep(timeTick)
            border=border+1

        drawData(data,getcolorArray(len(data), head, tail,border,j))
        time.sleep(timeTick)

    # swap pivot with border
    drawData (data,getcolorArray(len(data), head, tail,border,tail,True))
    time.sleep(timeTick)
           
    data[border], data[tail] = data[tail], data[border]

    return border


def quicksort(data,head,tail,drawData,timeTick):
    if head < tail:
        partitionindex = partition(data,head,tail,drawData,timeTick)

        #left partition
        quicksort(data,head,partitionindex-1,drawData,timeTick)

        #right partition
        quicksort(data,partitionindex+1,tail,drawData,timeTick)

def getcolorArray(datalen, head, tail ,border, curindx, isswapping = False):
    colorarray = []
    for i in range(datalen):
        # base coloring

        if i>=head and i<=tail:
            colorarray.append('gray')
        else:
            colorarray.append('white')

        if i==tail:
            colorarray[i]='blue'
        elif i== border:
            colorarray[i]='red'
        elif i== curindx:
            colorarray[i]= 'yellow'
        
        if isswapping:
            if i== border or i == curindx:
                colorarray[i] = 'green'

    return colorarray