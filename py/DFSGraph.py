# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def DFS(self,graph,v,visited):
        if visited[v]:
            return
        visited[v] = True
        print(v)
        for i in graph[v]:
            self.DFS(graph, i, visited)
        return

    def DFSGraph(self):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[],[0],[0,1]]
        for v in range(3):
            visited = [False for v in range(8)]
            self.DFS(graph,v,visited)
            print("$$$$$$")

        # 对各个顶点进行深度便利。
        for v in range(3):
            visited, stack = {}, [v]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited[node] = 1
                print(node)
                for j in graph[node]:
                    stack.append(j)
            print("###")

sol = Solution()
print(sol.DFSGraph())