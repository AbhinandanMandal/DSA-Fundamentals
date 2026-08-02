
# Deleting 1 indexed node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
temp3 = Node(40)
temp4 = Node(50)

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1

temp2.next = temp3
temp3.prev = temp2

temp3.next = temp4
temp4.prev = temp3


def DeleteNode(head, n):
    if head is None:
        return None

    if n == 1:
        head = head.next
        head.prev = None
        return head

    curr = head
    for _ in range(n-2):
        curr = curr.next

    node_to_delete = curr.next
    if node_to_delete.next:
        curr.next = node_to_delete.next
        node_to_delete.next.prev = curr
    else:
        curr.next = None
    return head


def PrintDLL(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next


head = DeleteNode(head, 3)
PrintDLL(head)
