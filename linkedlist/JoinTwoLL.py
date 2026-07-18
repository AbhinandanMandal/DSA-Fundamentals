
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)


head2 = Node(40)
head2.next = Node(50)


def JoinTwoLL(head1, head2):
    curr1 = head1
    curr2 = head2

    while curr1.next:
        curr1 = curr1.next
    curr1.next = curr2
    return head1


def PrintLinkedList(head1):
    curr = head1
    while curr:
        print(curr.data, end=" ")
        curr = curr.next


head1 = JoinTwoLL(head1, head2)
PrintLinkedList(head1)
