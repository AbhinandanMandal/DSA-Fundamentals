

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)
temp4 = Node(50)

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1

temp2.next = temp3
temp3.prev = temp2

temp3.next = temp4
temp4.prev = temp3

"""
def DisplayDLL(head):
    curr = head
    forward = []
    while curr:
        forward.append(curr.data)
        tail = curr
        curr = curr.next

    curr = tail
    backward = []
    while curr:
        backward.append(curr.data)
        curr = curr.prev

    return forward, backward


print(DisplayDLL(head))
"""


def printDLL(head):
    curr = head
    elements = []
    while curr:
        elements.append(curr.data)
        curr = curr.next
    return elements


print(printDLL(head))
