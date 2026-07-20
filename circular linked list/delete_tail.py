
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head


def DeleteTail(head):
    curr = head
    while curr.next.next != head:
        curr = curr.next
    curr.next = head
    return head


def PrintCircularLL(head):
    if head is None:
        return

    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next


head = DeleteTail(head)
PrintCircularLL(head)
