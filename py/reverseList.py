# Definition for singly-linked list.
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
        start, point, pre, new_head, ret_head = head, head, None, head.next, None  # start store current section head,point store next section head
        i = 1
        while point.next is not None:  # move point to next section head
            if i % k == 0:
                ret_head = point
            point = point.next
            if i % k == 0:
                break
            i += 1
        if i % k != 0:  # k > link list length
            return head
        cur = head
        while i % k == 0:
            start.next = new_head
            start = cur
            while cur.next != point:
                tmp = cur
                cur = cur.next
                tmp.next = pre
                pre = tmp
            cur.next = pre
            start.next = point
            cur = point
            i = 1
            while point.next is not None:
                if i % k == 0:
                    new_head = point
                point = point.next
                if i % k == 0:
                    break
                i += 1
        return ret_head



sol = Solution()
L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L1.next = L2
L2.next = L3
sol.reverseList(L1)
print('he')
