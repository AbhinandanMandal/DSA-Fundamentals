
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)

head2 = Node(10)
head2.next = Node(20)
head2.next.next = Node(30)
# head2.next.next.next = Node(40)


def IdenticalLinkedList(head1, head2):
    curr1 = head1
    curr1_length = 0
    while curr1:
        curr1 = curr1.next
        curr1_length += 1

    curr2 = head2
    curr2_length = 0
    while curr2:
        curr2 = curr2.next
        curr2_length += 1

    if curr1_length != curr2_length:
        return False

    else:
        curr1 = head1
        curr2 = head2
        while curr1 and curr2:
            if curr1.key != curr2.key:
                return False
            curr1 = curr1.next
            curr2 = curr2.next

    return True


print(IdenticalLinkedList(head1, head2))
