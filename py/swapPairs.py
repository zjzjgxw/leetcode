# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        newHead = head.next
        pre = ListNode(None)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return newHead
sol = Solution()
L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L1.next = L2
L2.next = L3
sol.swapPairs(L1)
print('he')
