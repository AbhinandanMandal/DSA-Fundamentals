

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head


def IsCircularLL(head):
    if head is None:
        return True

    curr = head
    while curr.next is not None and curr.next != head:
        curr = curr.next
    return curr.next == head


print(IsCircularLL(head))
