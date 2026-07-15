
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


def MiddleLinkedList(head):
    if head is None:
        return None

    count = 0
    curr = head
    while curr:
        curr = curr.next
        count += 1

    curr = head
    for _ in range(count//2):
        curr = curr.next
    print(curr.key)


MiddleLinkedList(head)
