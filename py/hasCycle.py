# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        p1, p2 = head, head.next
        while True:
            if p1 == p2:
                return True
            if p1 is None or p2 is None or p2.next is None:
                return False
            p1 = p1.next
            p2 = p2.next.next

sol = Solution()
L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L1.next = L2
L2.next = L3
sol.swapPairs(L1)
print('he')
