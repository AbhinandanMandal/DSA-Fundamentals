

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


def DeleteLastNode(head):
    if head is None:
        return None
    if head.next is None:
        return None
    else:
        curr = head
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        return head


def PrintDLL(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next


head = DeleteLastNode(head)
PrintDLL(head)
