"""
Finding a peak element:

Given an array of integers.Find a peak element in it. An array element is peak if it is
NOT smaller than its neighbors. For corner elements, we need to consider only one
neighbor. For example, for input array {5,10,20,15}, 20 is the only peak element.

"""


# A python 3 program to find a peak
# element using divide and conquer
def findPeakUtil(arr, low, high, n):

    # Find index of middle element
    # (low + high) /2
    mid = low + (high - low)/2
    mid = int(mid)

    # Compare middle element with its neighbors (if neighbours exist)
    if((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == n - 1 or arr[mid - 1] <= arr[mid])):
        return mid

    # If middle element is not peak and its left neighbour is greater than it,
    # than right half must have a peak element
    else:
        return findPeakUtil(arr, (mid + 1), high, n)


# A wrapper over recursive function findPeakUtil()
def findPeak(arr, n):

    return findPeakUtil(arr, 0, n -1, n)


# Driver code
arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))






