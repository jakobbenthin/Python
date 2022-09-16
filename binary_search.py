import random
import time

# Binary search algorithm

# prove binary is faster than naive search


# naive search: scan entire list and ask if its equal to the target
# if yes return index
# if no, return -1

def naive_search(l, search):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == search:
            return i
    return -1

# binary search uses divide and conquer
# we will leverage the fact that out list is SORTED

def binary_search(l, target, low=None, high=None):
    # example l = [1, 3, 5, 10, 12]
    if low is None:
        low = 0
    if high is None:
        high = len(l) -1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint -1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint +1, high)

if __name__ == '__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 2
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    # build a sorted list of length 10000
    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3* length))

    sorted_list = sorted(list(sorted_list))

    # Naive
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list,target)
    end = time.time()    
    print("Naive search time: ", (end - start)/length, "seconds")
    
    # Binary
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end = time.time()    
    print("Binary search time: ", (end - start)/length, "seconds")
