from typing import *

import self as self


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
            print("The list1 is empty.")


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        r = head
        l = dummy
        for i in range(n):
            r = r.next
        while r:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    list1 = LinkedList()
    list1.push_back(1)
    # list1.push_back(3)
    # list1.push_back(5)
    # list1.push_back(3)
    # list1.push_back(1)
    # list1.push_back(1)
    list1.PrintList()
    list1.head = s.removeNthFromEnd(list1.head, 1)
    list1.PrintList()
