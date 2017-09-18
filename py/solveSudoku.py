class Solution(object):
    def check(self, board, x, y, val):
        for i in range(9):
            if board[i][y] == val:
                return False
        for j in range(9):
            if board[x][j] == val:
                return False
        row = x - x % 3
        col = y - y % 3
        for i in range(3):
            for j in range(3):
                if board[row+i][col+j] == val:
                    return False
        return True

    def solve(self, borad, x, y):
        if x == 9:
            return True
        if y == 9:
            return self.solve(borad, x+1, 0)
        if borad[x][y] != '.':
            return self.solve(borad, x, y+1)
        for val in range(1, 10):
            if self.check(borad, x, y, str(val)):
                borad[x][y] = str(val)
                if self.solve(borad, x, y+1):
                    return True
                borad[x][y] = '.'
        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board, 0, 0)
