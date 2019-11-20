"""
Delete Middle Node:
Implement an algorithm to delete a node in the middle (i.e., any node but the first
and  last node, not necessary the exact middle) of a singly linked list, given only
access to that node.

EXAMPLE
Input: the node c from the linked list a -> b -> c -> d -> e -> f


"""
from linkedlist import linked_list


def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


ll = linked_list()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
delete_middle_node(middle_node)
print(ll)




