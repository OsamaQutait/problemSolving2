from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, dummy

        # Move fast k nodes ahead
        for _ in range(k):
            fast = fast.next

        first_pointer = fast

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        second_pointer = slow.next

        # Swap the nodes
        first_pointer.val, second_pointer.val = second_pointer.val, first_pointer.val

        return dummy.next




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

arr = [1,2,3,4,5]
linked_list1 = array_to_linked_list(arr)

k = 2
solution = Solution()
merge_head = solution.swapNodes(linked_list1, k)
display_linked_list(merge_head)