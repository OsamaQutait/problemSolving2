from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p1, p2, p = l1, l2, dummy
        carry = 0

        while p1 or p2 or carry:
            # Get the values from the current nodes (if available)
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            # Calculate the sum with the carry
            temp = val1 + val2 + carry

            # Update the carry for the next iteration
            carry = temp // 10

            # Create a new node with the current digit and move the pointers
            p.next = ListNode(temp % 10)
            p = p.next
            if p1: p1 = p1.next
            if p2: p2 = p2.next

        return dummy.next




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


l1 = [2,4,3]
l2 = [5,6,4]
linked_list1 = array_to_linked_list(l1)
linked_list2 = array_to_linked_list(l2)

# arr = [1,2,3,4,5]
# linked_list1 = array_to_linked_list(arr)

solution = Solution()
merge_head = solution.addTwoNumbers(linked_list1, linked_list2)
display_linked_list(merge_head)