class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = head


def DeleteKthNode(head, k):
    curr = head
    for _ in range(k-2):
        curr = curr.next
    curr.next = curr.next.next
    return head


def PrintCircularLL(head):
    if head is None:
        return

    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next


head = DeleteKthNode(head, 3)
PrintCircularLL(head)
