
def merge(input_list, low, mid, high):
    length_left_list = mid - low + 1
    length_right_list = high - mid

    # creating right and left temporary lists to store data
    left_temp_list = [0] * length_left_list
    right_temp_list = [0] * length_right_list

    # after ^, we would have [0,0,0,0] [0,0,0,0] for example.
    # Now we get elements from inp_list and put them into left and right temp lists based on indexes

    for i in range(0, length_left_list):
        left_temp_list[i] = input_list[low + i]

    for j in range(0, length_right_list):
        right_temp_list[j] = input_list[mid + 1 + j]

    # after ^, both the temp arrays will have data from input list. now lets compare those elements one by one
    #Need iterators for left, right and main lists

    i = 0 # iterate through left temp array
    j = 0 # iterate through right temp array
    k = 0 # iterate through main array

    while i < length_left_list and j < length_left_list:
        if left_temp_list[i] <= right_temp_list[j]:
            input_list[k] = left_temp_list[i]
            i += 1
        else:
            input_list[k] = right_temp_list[j]
            j += 1
        k += 1

    # copy remaining elements of left and right arrays
    while i < length_left_list:
        input_list[k] = left_temp_list[i]
        i += 1
        k += 1

    while j < length_right_list:
        input_list[k] = right_temp_list[j]
        j += 1
        k += 1

def merge_sort(input_list, left, right):
    if left < right:
        mid = (left + (right-1))//2

        merge_sort(input_list, left, mid)
        merge_sort(input_list, mid+1, right)

        merge(input_list, left, mid, right)


if __name__ == '__main__':
    test = [12,34,56,78,90,123,456,423,54,1245,67,1213,545,764,154, 987, 413]

    merge_sort(test, 0, len(test)-1)

    print(f"########### sorted list #############")
    print(test)






