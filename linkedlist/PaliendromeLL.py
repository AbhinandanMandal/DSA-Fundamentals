
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)


def isPalindrome(head):
    # code here
    data_list = []
    curr = head
    while curr:
        data_list.append(curr.data)
        curr = curr.next

    # [1,2,3,4,5]
    left = 0
    right = len(data_list)-1
    while left < right:
        if data_list[left] != data_list[right]:
            return False
        left += 1
        right -= 1
    return True


print(isPalindrome(head))
