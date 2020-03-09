
def bubble_sort(input_list):
    list_length = len(input_list)
    iterations = 0
    while iterations <= list_length - 1:
        for i in range(list_length - 1):
            if input_list[i] > input_list[i+1]:
                temp = input_list[i]
                input_list[i] = input_list[i+1]
                input_list[i + 1] = temp
        iterations += 1
        bubble_sort(input_list[:-iterations])
    return input_list




if __name__ ==  '__main__':
    test = [87,4,7,8,2,987,56,76,123,54,67,90,878,58]
    res = bubble_sort(test)
    print(f"sorted list is {res}")


