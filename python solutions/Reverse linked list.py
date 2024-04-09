class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# my method
class Solution:
    def reverseList(self, head):
        self.temp=head
        self.prev=None
        
        while self.temp!=None:
            self.front=self.temp.next
            self.temp.next=self.prev
            self.prev=self.temp
            self.temp=self.front
        return self.prev
    
# Helper function to print linked list
def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original linked list:")
printLinkedList(head)

# Reverse the linked list
solution = Solution()
reversed_head = solution.reverseList(head)

print("\nReversed linked list:")
printLinkedList(reversed_head)
