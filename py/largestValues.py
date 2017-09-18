# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        ret, level = [], [root]
        while level:
            maxNum = level[0].val
            for node in level:
                if maxNum < node.val:
                    maxNum = node.val
            ret.append(maxNum)
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ret

    #discuss看到的简化版
    def findValueMostElement(self, root):
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return maxes


