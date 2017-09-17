# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 0 or numCourses == 1:
            return True
        graph = [[] for i in range(numCourses)]
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        # 对各个顶点进行深度便利。
        for v in range(numCourses):
            visited, stack = {}, [v]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited[node] = 1
                for j in graph[node]:
                    stack.append(j)

sol = Solution()
numCourses = 4
prerequisites = [[1,0],[0,1],[3,2],[2,1],[3,1],[1,2]]
print(sol.canFinish(numCourses,prerequisites))