"""

Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides input array
in two halves, calls itself for the two halves and then merges the two sorted halves.
The merge() function is used for merging two halves. The merge(arr, l, m, r) is key
process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two
sorted sub-arrays into one. See following C implementation for details.

MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:
             middle m = (l+r)/2
     2. Call mergeSort for first half:
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)

The following diagram from wikipedia shows the complete merge sort process for an
example array {38, 27, 43, 3, 9, 82, 10}. If we take a closer look at the diagram,
we can see that the array is recursively divided in two halves till the size
becomes 1. Once the size becomes 1, the merge processes comes into action and
starts merging arrays back till the complete array is merged.
"""

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]   # Dividing the array elements
        R = arr[mid:]   # into 2 halves

        mergeSort(L)    # Sorting the first half
        mergeSort(R)    # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(arr):
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)




















