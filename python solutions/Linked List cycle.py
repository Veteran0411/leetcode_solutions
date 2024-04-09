import collections

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head) :
        a=collections.defaultdict()
        self.temp=head
        while self.temp!=None:
            if self.temp not in a:
                a[self.temp]=self.temp.val
            else:
                return True
            self.temp=self.temp.next
        return False
    
head=ListNode(3)
head.next=ListNode(2)
head.next.next=ListNode(0)
head.next.next.next=ListNode(-4)
head.next.next.next.next=head.next #creating cycle

sol=Solution()
print(sol.hasCycle(head))
