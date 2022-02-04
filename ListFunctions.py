# Various list functions with various task
#
# @author     Duran, Aaron
# @date       10/20/2021

# A
# Swap the first and last elements in the list.
def SwapFirstLast(list):
    i = list[0]
    list[0] = list[len(list) - 1]
    list[len(list) - 1] = i

    return list

# B
# Shift all elements by one to the right and move the last element into the first position
def ShiftOneRight(list):
    ShiftedList = [list[len(list) - 1]]
    for i in range(0, len(list) - 1):
        ShiftedList.append(list[i])

    return ShiftedList

# C
# Replace all even elements with 0
def ReplaceEvensZero(list):
    for i in range(0, len(list)):
        if list[i] % 2 == 0:
            list[i] = 0

    return list

# D
# Replace each element except the first and last by the larger of its two neighbors
def ReplaceWithLargestNeighbor(list):
    NewList = [list[0]]
    for i in range(1, len(list) - 1):
        neighbor1 = list[i - 1]
        neighbor2 = list[i + 1]
        NewList.append(max(neighbor1, neighbor2))
    NewList.append(list[len(list) - 1])

    return NewList

# E
# Remove the middle element if the list length is odd, or the middle two elements if the length is even.
def MiddleRemoved(list):
    length = len(list)
    HalfLength = int((length / 2))
    if length % 2 == 0:
        HalfLength = (int(HalfLength - 1))
        list.pop(HalfLength)
        list.pop(HalfLength)
    else:
        list.pop(HalfLength)

    return list

# F
# Move all even elements to the front, otherwise preserving the order of the elements.
def EvenToFront(list):
    odds = []
    evens = []
    for i in range(0, len(list)):
        if list[i] % 2 == 0:
            evens.append(list[i])
        else:
            odds.append(list[i])

    return evens + odds

# G
# Return the second-largest element in the list
def SecondLargestReturn(list):
    list.remove(max(list))

    return max(list)

# H
# Return true if the list is currently sorted in increasing order.
def IsIncreasingOrder(list):
    test = []
    for i in range(0, len(list)): # I couldn't find a more efficient way of doing this but i feel
        test.append(list[i])      # there is, can you please give me feedback if there is.
    test.sort()

    return test == list

# I
# Return true if the list contains two adjacent duplicate elements.
def HasAdjacentDuplicates(list):
    for i in range(1, len(list)):
        if list[i] == list[i - 1]:
            return True

    return False

# J
# Return true if the list contains duplicate elements (which need not be adjacent).
def HasDuplicates(list):
    for i in range(0, len(list)):
        for temp in range(i + 1, len(list)):
            if list[i] == list[temp]:
                return True

    return False


def main():
    print("example list for each function below")
    a = [1,2,3,4,5]
    print("A)", a)
    b = [1,2,3,4,5,6,7,8,9,10]
    print("B)", b)
    c = [2,3,2,3,2]
    print("C)", c)
    d = [10,20,70,40,50,60]
    print("D)", d)
    e = [1,2,3,4,5,6]
    print("E)", e)
    f = [3,4,2,7,9,11,10]
    print("F)", f)
    g = [2,3,66,23,777,233]
    print("G)", g)
    h = [10,34,68,90,466,3456]
    print("H)", h)
    i = [20,300,23,44,44,98]
    print("I)", i)
    j = [20,33,65,83,33,100]
    print("J)", j)

    print("A) Swapping the first and last element is:", SwapFirstLast(a))
    print("B) Shifting all elements to the right is:", ShiftOneRight(b))
    print("C) Replacing even elements with zero is:", ReplaceEvensZero(c))
    print("D) Replacing elements with larger neighbor is:", ReplaceWithLargestNeighbor(d))
    print("E) Removing the middle element(s) is:", MiddleRemoved(e))
    print("F) Moving all even elements to the front is:", EvenToFront(f))
    print("G) The second largest element on the list is:", SecondLargestReturn(g))
    print("H) Is the list currently in increasing order:", IsIncreasingOrder(h))
    print("I) Does the list have adjacent duplicates:", HasAdjacentDuplicates(i))
    print("J) Does the list have duplicates:", HasDuplicates(j))


main()
