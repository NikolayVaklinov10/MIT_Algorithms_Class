"""
Return Kth to Lost: Implement an algorithm to find the kth to last element of a singly
linked list.
"""


from linkedlist import linked_list


def kth_to_last(ll, k):
    runner = current = ll.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current


ll = linked_list()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 3))


