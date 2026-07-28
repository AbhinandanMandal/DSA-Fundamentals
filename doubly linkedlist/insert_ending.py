
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1


def InsetEnd(head, data):

    temp = Node(data)
    if head is None:
        return temp

    curr = head
    while curr.next != None:
        curr = curr.next

    curr.next = temp
    temp.prev = curr
    return head


def Traversal(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next


head = InsetEnd(head, 40)
Traversal(head)
