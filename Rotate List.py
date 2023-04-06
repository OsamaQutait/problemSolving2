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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        p, length, p1 = head, 1, head
        while p.next:
            p = p.next
            length += 1
        k = k % length
        if k == 0:
            return head
        for i in range(length-k-1):
            p1 = p1.next
        newHead = p1.next
        p1.next = None
        p.next = head
        return newHead
if __name__ == '__main__':
    s = Solution()
    list1 = LinkedList()
    list1.push_back(1)
    list1.push_back(3)
    list1.push_back(5)
    list1.push_back(3)
    list1.push_back(1)
    list1.push_back(1)
    list1.PrintList()
    list1.head = s.rotateRight(list1.head, 3)
    list1.PrintList()

