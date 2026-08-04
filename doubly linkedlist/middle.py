
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


def findMiddle(head):
    # code here
    # This block of code is for finding the length of dll
    len_dll = 0
    curr = head
    while curr:
        curr = curr.next
        len_dll += 1

    if len_dll == 1:
        return head

    curr = head
    for _ in range(len_dll//2):
        curr = curr.next
    return curr.data


print(findMiddle(head))
