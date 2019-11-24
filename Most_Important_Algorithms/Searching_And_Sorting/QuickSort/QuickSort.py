"""

Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as
pivot and partitions the given array around the picked pivot. There are many different
versions of quickSort that pick pivot in different ways.

    1. Always pick first element as pivot.
    2. Always pick last element as pivot (implemented below)
    3. Pick a random element as pivot.
    4. Pick median as pivot.


The key process in quickSort is partition(). Target of partitions is, given an array
and an element x of array as pivot, put x at its correct position in sorted array
and put all smaller elements (smaller than x) before x, and put all greater elements
(greater than x) after x. All this should be done in linear time.


Pseudo Code for recursive QuickSort function:

/* low  --> Starting index,  high  --> Ending index */
quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[pi] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}

Partition Algorithm

There can be many ways to do partition, following pseudo code adopts the method
given in CLRS book. The logic is simple, we start from the leftmost element and
keep track of index of smaller (or equal to) elements as i. While traversing, if
we find a smaller element, we swap current element with arr[i]. Otherwise we
ignore current element.

"""

# Python program for implementation of Quick Sort algorithm

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to fight of pivot


def partition(arr, low, high):
    i = (low-1)     # index of smaller element
    pivot = arr[high]
    for j in range(low, high):
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),































