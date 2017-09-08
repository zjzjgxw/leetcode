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
        p1, p2 = head, head.next
        pre = ListNode(None)
        pre.next = p1
        i = 1
        while p1.next is not None and p2 is not None:
            if i % 2 == 1:
                tmp = p1
                p1.next = p2.next
                p2.next = tmp
                pre.next = p2
                p2 = p1.next
            else:
                pre = p1
                p1 = p1.next
                p2 = p2.next
            i += 1
        return newHead
sol = Solution()
L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L1.next = L2
L2.next = L3
sol.swapPairs(L1)
print('he')
