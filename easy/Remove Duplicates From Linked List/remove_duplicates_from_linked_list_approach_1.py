# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    first = linkedList
    while first is not None:
        second = first.next
        while second != None and second.value == first.value:
            second = second.next
        first.next = second
        first = second
    return linkedList
