

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


head = Node(10)


def LengthDLL(head):
    curr = head
    length = 0
    while curr:
        curr = curr.next
        length += 1
    return length


print(LengthDLL(head))
