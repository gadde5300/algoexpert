# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    second = head
    count = 1
    while second.next is not None:
        second = second.next
        count += 1
    reach = count-k
    first = head
    if reach != 0:
        while first.next is not None and reach != 1:
            reach -= 1
            first = first.next
        first.next = first.next.next
    else:
        first = first.next
        head.value = first.value
        head.next = first.next
        
        
