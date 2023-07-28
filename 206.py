from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = tmp = None
        while head:
            tmp = head
            head = head.next
            tmp.next = prev
            prev = tmp
        return tmp


list_node = ListNode(val=1)
list_node.next = ListNode(val=2)
list_node.next.next = ListNode(val=3)
list_node.next.next.next = ListNode(val=4)
list_node.next.next.next.next = ListNode(val=5)

s = Solution()
res = s.reverseList(list_node)
while res:
    print(res.val)
    res = res.next
