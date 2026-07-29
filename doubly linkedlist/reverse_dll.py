
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


def ReverseDLL(head):
    stack_data = []
    curr = head
    while curr:
        stack_data.append(curr.data)
        curr = curr.next
    curr = head
    while curr:
        curr.data = stack_data.pop()
        curr = curr.next
    return head


def PrintDLL(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next


head = ReverseDLL(head)
PrintDLL(head)
