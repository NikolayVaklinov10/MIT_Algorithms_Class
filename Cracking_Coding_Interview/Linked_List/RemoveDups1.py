"""
Remove Dups:
Write code to remove duplicates from a unsorted linked list.
FOLLOW UP

How would you solve this problem if a temporary buffer is not
allowed?
"""
from linkedlist import linked_list


def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return ll


# second option
def remove_dups_followup(ll):
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return ll.head


ll = linked_list()
ll.generate(100, 0, 9)
print(ll)
remove_dups(ll)
print(ll)

ll.generate(100, 0, 9)
print(ll)
remove_dups_followup(ll)
print(ll)








