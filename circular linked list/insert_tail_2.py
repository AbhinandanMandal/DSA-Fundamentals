
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head


def InsertTail(head, n):

    temp = Node(n)
    curr = head
    while curr.next != head:
        curr = curr.next
    temp.next = curr.next
    curr.next = temp
    return head


def PrintCircular(head):
    if head is None:
        return

    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next


head = InsertTail(head, 15)
PrintCircular(head)
