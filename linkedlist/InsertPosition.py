
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


def insertAtPosition(head, pos, data):
    ll_length = 0
    curr = head
    while curr:
        ll_length += 1
        curr = curr.next

    curr = head
    temp = Node(data)

    if pos > ll_length:
        return head

    for _ in range(pos-1):
        curr = curr.next

    temp.next = curr.next
    curr.next = temp
    return head


def PrintLinkedList(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next


head = insertAtPosition(head, 2, 15)
PrintLinkedList(head)
