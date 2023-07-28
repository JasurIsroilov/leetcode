from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return head.next


list_node1 = ListNode(val=1)
list_node1.next = ListNode(val=2)
list_node1.next.next = ListNode(val=4)

list_node2 = ListNode(val=1)
list_node2.next = ListNode(val=3)
list_node2.next.next = ListNode(val=4)

# list_node1 = None
# list_node2 = ListNode()

s = Solution()
res = s.mergeTwoLists(list_node1, list_node2)

while res:
    print(res)
    res = res.next
