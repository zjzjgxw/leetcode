class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def find(board, i, j, word, cur):
            if cur == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
                return False
            if board[i][j] != word[cur]:
                return False
            tmp = board[i][j]
            board[i][j] = '#'

            isFind = find(board, i + 1, j, word, cur + 1) or find(board, i - 1, j, word, cur + 1) or find(board, i,
                                                                                                          j + 1, word,
                                                                                                          cur + 1) or find(
                board, i, j - 1, word, cur + 1)
            board[i][j] = tmp
            return isFind

        if board is None:
            return False
        if len(word) <= 0:
            return True
        for i in range(len(board)):
            for j in range(len(board[i])):
                if find(board, i, j, word, 0):
                    return True
        return False

word = 'A'
word[0] += '0'
print(word)