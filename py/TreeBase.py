class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def banaryTree(self, root):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def preDFS(root):
            if root is None:
                return
            print(root.val)
            preDFS(root.left)
            preDFS(root.right)

        def midDFS(root):
            if root is None:
                return
            midDFS(root.left)
            print(root.val)
            midDFS(root.right)

        def afterDFS(root):
            if root is None:
                return
            afterDFS(root.left)
            afterDFS(root.right)
            print(root.val)

        def BFS(root):
            queue = [root]
            while queue:
                node = queue.pop(0)
                if node is None:
                    continue
                print(node.val)
                queue.append(node.left)
                queue.append(node.right)

        def BFS2(root):
            level = [root]
            while level:
                for node in level:
                    print(node.val)
                level = [kid for n in level for kid in (n.left, n.right) if kid]

        if root is None:
            return
        preDFS(root)
        print('####')
        midDFS(root)
        print('#####')
        afterDFS(root)
        print('@@@@@')
        BFS(root)
        print('#####')
        BFS2(root)

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node6.left = node8
node6.right = node9
node7.right = node10
sol = Solution()
sol.banaryTree(node1)
