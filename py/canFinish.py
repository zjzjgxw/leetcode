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
        def DFS(graph, v, visited):
            if visited[v]:
                return False
            visited[v] = True
            for j in graph[v]:
                if not DFS(graph, j, visited):
                    return False
            visited[v] = False
            return True

        if numCourses == 0 or numCourses == 1:
            return True
        graph = [[] for i in range(numCourses)]
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        # 对各个顶点进行深度便利。
        visited = [False for i in range(numCourses)]
        for v in range(numCourses):
            if not DFS(graph, v, visited):
                return False
        return True


sol = Solution()
numCourses = 4
prerequisites = [[1,0],[0,1],[3,2],[2,1],[3,1],[1,2]]
print(sol.canFinish(numCourses,prerequisites))