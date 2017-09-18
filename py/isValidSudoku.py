class Solution(object):
    def checkRow(self, board, row):
        buff_dic = {}
        for i in range(9):
            if board[row][i] in buff_dic:
                return False
            if board[row][i] != '.':
                buff_dic[board[row][i]] = True
        return True

    def checkCol(self, board, col):
        buff_dic = {}
        for i in range(9):
            if board[i][col] in buff_dic:
                return False
            if board[i][col] != '.':
                buff_dic[board[i][col]] = True
        return True

    def checkSquare(self, board, row, col):
        buff_dic = {}
        for i in range(3):
            for j in range(3):
                if board[row+i][col+j] in buff_dic:
                    return False
                if board[row+i][col+j] != '.':
                    buff_dic[board[row+i][col+j]] = True
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if not self.checkRow(board,i):
                return False
        for j in range(9):
            if not self.checkCol(board,j):
                return False
        square = [[i, j] for i in range(9) for j in range(9) if i % 3 == 0 and j % 3 == 0]
        for point in square:
            if not self.checkSquare(board,point[0],point[1]):
                return False
        return True
