
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


def InsertMiddle(head, x):
    temp = Node(x)
    if head is None:
        return temp

    curr = head
    ll_length = 0
    while curr:
        ll_length += 1
        curr = curr.next

    curr = head
    for _ in range((ll_length-1)//2):
        curr = curr.next
    temp.next = curr.next
    curr.next = temp
    return head


def PrintLinkedList(head):
    curr = head
    while curr:
        print(curr.key, end=" ")
        curr = curr.next


head = InsertMiddle(head, 15)
PrintLinkedList(head)
