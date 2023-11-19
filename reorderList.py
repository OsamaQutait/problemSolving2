from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        # Find the middle of the linked list
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Merge the two halves of the linked list
        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2

        return head








def array_to_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head

def display_linked_list(head):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    print(" -> ".join(map(str, elements)))

#if __name__ == '__main':
# Example usage to convert an array to a linked list

arr = [1,2,3,4,5]
linked_list1 = array_to_linked_list(arr)

solution = Solution()
solution.reorderList(linked_list1)
display_linked_list(linked_list1)