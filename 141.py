from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        elems = set()
        if head is None:
            return False
        while head.next is not None:
            if head in elems:
                return True
            elems.add(head)
            head = head.next
        return False


head = [3,2,0,-4]
pos = 1

node = ListNode(3)
node.next = ListNode(2)
node.next.next = ListNode(0)
node.next.next.next = ListNode(-4)
node.next.next.next.next = node.next

s = Solution()
print(s.hasCycle(node))
