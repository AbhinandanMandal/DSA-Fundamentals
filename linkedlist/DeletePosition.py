
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

"""
def InsertPosition(head, key, pos):
    temp = Node(key)
    curr = head

    if pos == 1:
        temp.next = curr
        return temp

    for _ in range(pos-2):
        curr = curr.next

    temp.next = curr.next
    curr.next = temp
    return head
"""


def DeletePosition(head, pos):
    curr = head
    if pos == 1:
        return curr.next
    for _ in range(pos - 2):
        curr = curr.next
    curr.next = curr.next.next
    return head


def PrintLinkedList(head):
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


head = DeletePosition(head, 3)
PrintLinkedList(head)
