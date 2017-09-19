class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix is None:
            return [[]]
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ret = []
        for i in range(len(matrix)):
            ret.append([])
            for j in range(len(matrix[i])):
                ret[i].append(0)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    continue
                #BFS
                level = [(i, j)]
                visited = {}
                distance = 0
                while level:
                    hasZero = False
                    for node in level:
                        if node in visited:
                            continue
                        if matrix[node[0]][node[1]] == 0:
                            hasZero = True
                            break
                        visited[node] = True
                    if hasZero:
                        break
                    distance += 1
                    tmp = []
                    for node in level:
                        for direct in direction:
                            x = node[0] + direct[0]
                            y = node[1] + direct[1]
                            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[i]):
                                continue
                            tmp.append((x, y))
                    level = tmp
                ret[i][j] = distance
        return ret


sol = Solution()
print(sol.updateMatrix([]))