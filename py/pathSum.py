# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        def DFS(root, sum, queue, ret):
            if root is None:
                return
            if root.right is None and root.left is None and sum == root.val:
                queue.append(root.val)
                ret.append(queue[:])
                queue.pop()
                return
            queue.append(root.val)
            DFS(root.left, sum-root.val, queue, ret)
            DFS(root.right, sum-root.val, queue, ret)
            queue.pop()
        DFS(root, sum, [], ret)
        return ret