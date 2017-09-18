class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def check(queen, row, col, n):
            for i in range(n):
                if i == col:
                    continue
                if queen[row][i] == 'Q':
                    return False
            for i in range(n):
                if i == row:
                    continue
                if queen[i][col] == 'Q':
                    return False
            for i in range(1, n):
                if row+i < n and col+i < n:
                    if queen[row+i][col+i] == 'Q':
                        return False
                else:
                    break
            for i in range(1, n):
                if row-i >= 0 and col-i >= 0:
                    if queen[row-i][col-i] == 'Q':
                        return False
                else:
                    break
            for i in range(1, n):
                if row+i < n and col-i >= 0:
                    if queen[row+i][col-i] == 'Q':
                        return False
            for i in range(1, n):
                if row-i >=0 and col+i < n:
                    if queen[row-i][col+i] == 'Q':
                        return False
            return True

        def slove(res, queen, row, n):
            if row == n:
                tmp = [''.join(i) for i in queen]
                res.append(tmp)
                return
            for col in range(n):
                if check(queen, row, col, n):
                    queen[row][col] = 'Q'
                    slove(res, queen, row+1, n)
                    queen[row][col] = '.'

        if n == 0:
            return [[]]
        queen = []
        for i in range(n):
            queen.append([])
            for j in range(n):
                queen[i].append('.')
        res = []
        slove(res, queen, 0, n)
        return res
