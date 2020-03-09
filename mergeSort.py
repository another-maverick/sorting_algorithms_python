# Working
def mergeSort(myList):
    if len( myList ) > 1:
        mid = len( myList ) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        i = 0  # iterate through left temp array
        j = 0  # iterate through right temp array
        k = 0  # iterate through main array

        while i < len( left ) and j < len( right ):
            if left[i] < right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1
        print(myList)
        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        print( myList )
        while j < len( right ):
            myList[k] = right[j]
            j += 1
            k += 1
        print(myList)


myList = [4,7,8,2,987,56,76,123,54,67,90,878]
mergeSort( myList )
print( myList )