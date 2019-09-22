
def partition(myArr, low, high):

    pivot = myArr[low]
    i = low
    j = high
    print("pivot is -- " + str(pivot))
    print("high element is --" + str(myArr[high]))

    while i < j:
        while True:
            i += 1
            if (myArr[i] > pivot) or (i == len(myArr)-1):
                break
        while myArr[j] > pivot:
            j -= 1
            #if (myArr[j] <= pivot) or (j == 0):
               # break
        if i < j:
            temp = myArr[i]
            myArr[i] = myArr[j]
            myArr[j] = temp
    temp1 = myArr[low]
    myArr[low] = myArr[j]
    myArr[j] = temp1
    print( "sorting in progress ----- " + str(myArr))
    return j



def quick_sort(myArr, low, high):
    if low < high:
        j = partition(myArr, low, high)
        quick_sort( myArr, low, j)
        quick_sort(myArr, j+1, high)





myArr = [4, 6, 3, 2, 1, 7, 5, 9, 8, 20, 34, 66, 51, 67, 55, 123, 435, 543, 666, 112, 344]
print("Before sorting ----- " + str(myArr))
quick_sort(myArr, 0, len(myArr) - 1)
print("After sorting ----- " + str(myArr))