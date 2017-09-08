class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        i, longest = 0, 0
        arr = []
        while i < len(s):
            if s[i] == '(':
                arr.append(i)  # push index in stack
            else:
                if len(arr) > 0:
                    if s[i] == ')' and s[arr[len(arr)-1]] == '(':  # if stack top element is '(' stack pop
                        arr.pop()
                    else:
                        arr.append(i)
                else:
                    arr.append(i)
            i += 1
        if len(arr) == 0:
            return len(s)  # if stack is empty,the string is all paired. so the length of string is longest.
        a, b = len(s), 0
        while len(arr) != 0:
            b = arr.pop()
            longest = max(longest, a-b-1)
            a = b
        longest = max(longest, a)
        return longest


sol = Solution()
print(sol.longestValidParentheses('()()(())(()'))

