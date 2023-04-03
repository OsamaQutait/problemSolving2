from typing import *


# node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Add new element at the end of the list2
    def push_back(self, newElement):
        newNode = Node(newElement)
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
    def reverseList(self, head: Optional[Node]) -> Optional[Node]:
        prev, curr = None, head
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        return prev


if __name__ == '__main__':
    list = LinkedList()
    list.push_back(1)
    list.push_back(2)
    list.push_back(3)
    list.push_back(4)
    list.push_back(5)
    list.push_back(6)
    list.PrintList()
    s = Solution()
    list.head = s.reverseList(list.head)
    list.PrintList()
