
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = head


def Insert_K(head, data, pos):
    curr = head
    temp = Node(data)

    if head is None:
        temp.next = temp
        return temp

    circular_length = 1
    while curr.next != head:
        circular_length += 1
        curr = curr.next

    if (pos > circular_length):
        return

    else:
        for _ in range(pos):
            curr = curr.next
        temp.next = curr.next
        curr.next = temp
        return head


def PrintCircularLL(head):
    if head is None:
        return

    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next


head = Insert_K(head, 15, 4)
PrintCircularLL(head)
