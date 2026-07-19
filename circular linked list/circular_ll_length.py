
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head


def CircularLength(head):
    length = 1
    curr = head.next
    while curr != head:
        length += 1
        curr = curr.next
    return length


print(CircularLength(head))
