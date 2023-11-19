from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Calculate the length of the linked list
        counter = 0
        p = head
        while p:
            counter += 1
            p = p.next

        # Calculate the position to remove
        position_to_remove = counter - n

        # Handle the case where the head needs to be removed
        if position_to_remove == 0:
            return head.next

        # Traverse to the node before the one to be removed
        p = head
        for _ in range(position_to_remove - 1):
            p = p.next

        # Remove the node
        if p.next and p.next.next:
            p.next = p.next.next
        elif not p.next:
            return None
        elif not p.next.next:
            p.next = None

        return head


# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode()
#         dummy.next = head
#         slow, fast = dummy, dummy
#         for _ in range(n + 1):
#             fast = fast.next
#         while fast:
#             fast = fast.next
#             slow = slow.next
#         slow.next = slow.next.next
#         return dummy.next




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

arr = [1]
linked_list1 = array_to_linked_list(arr)

n = 1
solution = Solution()
merge_head = solution.removeNthFromEnd(linked_list1, n)
display_linked_list(merge_head)