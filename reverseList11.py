class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


def display_linked_list(head):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    print(" -> ".join(map(str, elements)))

# if __name__ == '__main':
# Create an empty linked list
my_linked_list = ListNode()
head = my_linked_list

# Append the elements [1, 2, 3, 4, 5] to the linked list
data = [1, 2, 3, 4, 5]
for item in data:
    my_linked_list.next = ListNode(item)
    my_linked_list = my_linked_list.next

# Display the linked list
display_linked_list(head.next)  # Output: 1 -> 2 -> 3 -> 4 -> 5

# Example of reversing the linked list
solution = Solution()
reversed_head = solution.reverseList(head.next)
display_linked_list(reversed_head)  # Output: 5 -> 4 -> 3 -> 2 -> 1
