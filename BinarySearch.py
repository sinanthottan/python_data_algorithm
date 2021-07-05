from util import time_it

def linear_search(number,list):
    for index,value in enumerate(list):
        if value == number:
            return index
    return "Number not found"

def binary_search(number,list):
    left_index = 0
    right_index = len(list)-1
    mid_index = 0


    while left_index <= right_index:
        mid_index = (right_index+left_index)
        mid_number = list[mid_index]

        if mid_number == number:
            return mid_index;

        if mid_number < number:
            left_index = mid_index+1
        else:
            right_index = mid_index-1

    return "Number not found"

@time_it
def binary_search_recursion(number,list,left_index,right_index):
    if right_index < left_index:
        return "Number not found"
    mid_index = (right_index+left_index)//2
    mid_number = list[mid_index]
    if mid_number == number:
        return mid_index

    if mid_number < number:
        left_index = mid_index+1
    else:
        right_index = mid_index-1

    return binary_search_recursion(number,list,left_index,right_index)


if __name__ == '__main__':
    list = [2,3,12,7,23,35,44,67]
    method = input("Enter the method, 0.Linear Search, 1.Binary Search, 2.Binary Search with recursion: ")
    number = 44
    #print(binary_search_recursion(number,list,0,len(list)-1))
    if method == 0:
        print(linear_search(number,list))
    elif method == 1:
        print(binary_search(number,list))
    elif method == 2:
        print(binary_search_recursion(number,list,0,len(list)-1))
    else:
        print("Invalid Method")
