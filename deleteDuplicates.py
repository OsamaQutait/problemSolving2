from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        while pointer and pointer.next:
            if pointer.next.val == pointer.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
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

arr = [1,1,2,3,3]
linked_list1 = array_to_linked_list(arr)

val = 6
solution = Solution()
merge_head = solution.deleteDuplicates(linked_list1)
display_linked_list(merge_head)