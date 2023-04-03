from typing import *
# node structure
class ListNode:
  def __init__(self, val = 0):
    self.val = val
    self.next = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list2
  def push_back(self, newElement):
    newNode = ListNode(newElement)
    if(self.head == None):
      self.head = newNode
      return
    else:
      temp = self.head
      while(temp.next != None):
        temp = temp.next
      temp.next = newNode

  #display the content of the list2
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list2 contains:", end=" ")
      while (temp != None):
        print(temp.val , end=" ")
        temp = temp.next
      print()
    else:
      print("The list2 is empty.")