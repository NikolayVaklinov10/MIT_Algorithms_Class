"""
Partition:
Write a code to partition a linked list around a value x, such that all nodes less
than x come before all nodes greater than or equal to x. If x is contained within the
list, the values of x only need to be after the elements less than x (see below). The
partition element x can appear anywhere in the "right partition"; it does not need to
appear between the left and right partitions.

EXAMPLE
Input   3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

from linkedlist import linked_list


def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = nextNode

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None


ll = linked_list()
ll.generate(10, 0, 99)
print(ll)
partition(ll, ll.head.value)
print(ll)




