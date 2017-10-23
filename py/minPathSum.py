class Solution(object):
    def minPathSumRecursion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def minPath(grid, i, j):
            if i == len(grid) -1 and j == len(grid[i])-1:
                return grid[i][j]
            if i == len(grid)-1:
                return grid[i][j] + minPath(grid, i, j+1)
            if j == len(grid[i])-1:
                return grid[i][j] + minPath(grid, i+1, j)
            right = minPath(grid, i, j+1)
            down = minPath(grid, i+1, j)
            return grid[i][j] + min(down, right)

        if grid is None:
            return 0
        return minPath(grid, 0, 0)

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None:
            return 0
        res = [[0 for j in range(len(grid[i]))] for i in range(len(grid))]
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[i])-1, -1, -1):
                if i == len(grid)-1 and j == len(grid[i])-1:
                    res[i][j] = grid[i][j]
                    continue
                if i == len(grid)-1:
                    res[i][j] = grid[i][j] + res[i][j+1]
                    continue
                if j == len(grid[i])-1:
                    res[i][j] = grid[i][j] + res[i+1][j]
                    continue
                res[i][j] = grid[i][j] + min(res[i][j+1], res[i+1][j])
        return res[0][0]


sol = Solution()

