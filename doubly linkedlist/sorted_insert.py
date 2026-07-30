

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


# Function to insert a node in a sorted doubly linked list.
def sortedInsert(head, x):
    # code here
    temp = Node(x)
    if head is None:
        return temp

    # when x is less than head.data
    if temp.data < head.data:
        temp.next = head
        head.prev = temp
        return temp

    curr = head
    while curr and curr.data < temp.data:
        curr = curr.next

    # Last node condition
    if curr is None:
        last = head
        while last.next:
            last = last.next
        last.next = temp
        temp.prev = last
        return head

    temp.next = curr.next
    curr.next = temp
    curr.next.prev = temp
    temp.prev = curr
    return head


def PrintDLL(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next


head = sortedInsert(head, 45)
PrintDLL(head)
