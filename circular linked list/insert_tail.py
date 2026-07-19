
# Insert tail in O(1) time complexity
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head


def InsertEnd(head, x):
    temp = Node(x)
    if head is None:
        temp.next = temp
        return temp

    temp.next = head.next
    head.next = temp

    temp.data, head.data = head.data, temp.data
    return temp


def PrintCircularLL(head):
    if head is None:
        return

    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next


head = InsertEnd(head, 5)
PrintCircularLL(head)
