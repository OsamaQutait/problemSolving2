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
            print("The list1 is empty.")


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow, prev = head.next, head, None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        current1 = head
        current2 = prev

        while current1 and current2:
            next1 = current1.next
            next2 = current2.next
            current1.next = current2
            current2.next = next1
            current1 = next1
            current2 = next2
        while head:
            print(head.val, end=" ")
            head = head.next
        return None

if __name__ == '__main__':
    s = Solution()
    list1 = LinkedList()
    list1.push_back(1)
    list1.push_back(2)
    list1.push_back(3)
    list1.push_back(4)
    list1.push_back(5)
    list1.push_back(16)
    list1.push_back(11)
    # list1.PrintList()
    s.reorderList(list1.head)
    # list1.PrintList()
