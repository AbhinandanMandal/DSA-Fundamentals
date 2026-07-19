
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head


def InsertBeginning(head, n):
    temp = Node(n)
    curr = head

    if head is None:
        temp.next = temp
        return temp

    while curr.next != head:
        curr = curr.next
    curr.next = temp
    temp.next = head
    return temp


def PrintCircularLL(head):
    if head is None:
        return

    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next


head = InsertBeginning(head, 5)
PrintCircularLL(head)

# This is O(n) way of solving stuffs
