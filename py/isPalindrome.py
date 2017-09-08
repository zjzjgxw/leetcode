import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 0:
            return True
        i = 0
        j = len(s)-1
        s = s.lower()
        while i < j:
            while i <= len(s)-1 and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
            if i > len(s)-1 or j < 0:
                break
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def isPalindromeTwo(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 0:
            return True
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        if s == s[::-1]:
            return True
        return False


sol = Solution()
print(sol.isPalindromeTwo('A man, a plan, a canal: Panama'))
