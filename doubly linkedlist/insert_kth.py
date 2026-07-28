
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1


def InsertPosK(head, pos, x):
    temp = Node(x)
    if head is None:
        return temp

    curr = head
    for _ in range(pos):
        if curr.next is None:
            break
        curr = curr.next

    temp.next = curr.next
    temp.prev = curr

    if curr.next is not None:
        curr.next.prev = temp

    curr.next = temp
    return head


def Traversal(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next


head = InsertPosK(head, 2, 15)
Traversal(head)
