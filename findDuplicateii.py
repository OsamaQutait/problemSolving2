from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = {}
        for num in nums:
            if num not in h:
                h[num] = 1
            else:
                return num




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

nums = [1, 3, 4, 2, 2]
solution = Solution()
merge_head = solution.findDuplicate(nums)
display_linked_list(merge_head)