class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def add_node(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printLinkedList(self, head):
        if head == None:
            return
        # print(head.data)
        self.printLinkedList(head.next)
        print(head.data)
    def reverseList(self, head):
        previous, current = None, head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous


if __name__ == "__main__":
    list = LinkedList()
    list.add_node(1)
    list.add_node(2)
    list.add_node(3)
    list.add_node(4)
    list.printLinkedList(list.head)
    print("***")
    list.reverseList(list.head)
    list.printLinkedList(list.head)


