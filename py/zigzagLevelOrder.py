# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ans, level = [], [root]
        curDepth = 1
        while level:
            if curDepth % 2 == 0:
                ans.append([node.val for node in level[::-1]])
            else:
                ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
            curDepth += 1
        return ans
