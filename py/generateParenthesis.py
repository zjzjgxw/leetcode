class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def DFS(strings, left, right, n, ret):
            if len(strings) == n*2:
                ret.append(strings)
                return
            if left < n:
                DFS(strings+'(', left+1, right, n, ret)
            if right < left:
                DFS(strings+')', left, right+1, n, ret)

        if n == 0:
            return [""]
        ret, strings = [], ''
        DFS(strings, 0, 0, n, ret)
        return ret

sol = Solution()
print(sol.generateParenthesis(4))