# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

class Solution(object):
    maxSum = -sys.maxsize-1

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxSumRootToLeaf(root):
            if root is None:
                return 0
            left = max(0, maxSumRootToLeaf(root.left))
            right = max(0, maxSumRootToLeaf(root.right))
            self.maxSum = max(self.maxSum, left+right+root.val)
            return root.val + max(maxSumRootToLeaf(root.left), maxSumRootToLeaf(root.right))

        maxSumRootToLeaf(root)
        return self.maxSum

