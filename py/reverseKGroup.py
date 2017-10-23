class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        if k == 1:
            return head
        ret_head = ListNode(0)
        ret_head.next = head
        pre, tail = ret_head, ret_head
        while True:
            count = k
            while count > 0 and tail:
                count -= 1
                tail = tail.next
            if tail is None:
                break
            next_head = pre.next
            while pre.next != tail:
                temp = pre.next
                pre.next = temp.next
                temp.next = tail.next
                tail.next = temp
            pre, tail = next_head, next_head
        return ret_head.next

L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L4 = ListNode(4)
L5 = ListNode(5)
L6 = ListNode(6)
L7 = ListNode(7)
L1.next = L2
L2.next = L3
L3.next = L4
L4.next = L5
L5.next = L6
L6.next = L7
sol = Solution()
sol.reverseKGroup(L1, 3)
