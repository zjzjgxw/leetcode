class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        for i in range(len(matrix)):
            matrix[i].reverse()
        print(matrix)

sol = Solution()
sol.rotate([[1,2,3],[4,5,6],[7,8,9]])

