

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


def DeleteHead(head):
    if head is None:
        return None
    if head.next is None:
        return None

    else:
        head = head.next
        head.prev = None

    return head


def PrintDLL(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next


head = DeleteHead(head)
PrintDLL(head)
