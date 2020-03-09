# Best O(n)
# Average O(n^2)
# Worst O(n^2)
# simple one but does not perform well
def insertion_sort(inp_list):
    list_length = len(inp_list)

    for i in range(1, list_length-1):
        j = i
        while j > 0 and inp_list[j-1] > inp_list[j]:
            temp = inp_list[j-1]
            inp_list[j-1] = inp_list[j]
            inp_list[j] = temp
            j -= 1
        print(f"i is {i} and input list is {inp_list}")
    return inp_list


if __name__ == '__main__':
    test = [87,4,7,8,2,987,56,76,123,54,67,90,878,58,432,421,456,543,467,468,496,430]
    res = insertion_sort(test)
    print(f"######### \nsorted list is {res}")
