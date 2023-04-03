from typing import *


# node structure
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# class Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Add new element at the end of the list2
    def push_back(self, newElement):
        newNode = ListNode(newElement)
        if (self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = newNode

    # display the content of the list2
    def PrintList(self):
        temp = self.head
        if (temp != None):
            print("The list2 contains:", end=" ")
            while (temp != None):
                print(temp.val, end=" ")
                temp = temp.next
            print()
        else:
            print("The list2 is empty.")


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                n1.next = list2
                list2 = list2.next
            else:
                n1.next = list1
                list1 = list1.next
            n1 = n1.next
        if list1:
            n1.next = list1
        elif list2:
            n1.next = list2
        return n2.next


if __name__ == '__main__':
    s = Solution()
    list1 = LinkedList()
    list1.push_back(1)
    list1.push_back(3)
    list1.push_back(5)

    list2 = LinkedList()
    list2.push_back(2)
    list2.push_back(4)
    list2.push_back(6)

    list1.head = s.mergeTwoLists(list1.head, list2.head)
    list1.PrintList()
