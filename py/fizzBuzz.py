class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr = []
        if n <= 0:
            return arr
        for i in range(n):
            tmp = str(i+1)
            if (i+1) % 3 == 0 and (i+1) % 5 != 0:
                tmp = 'Fizz'
            elif (i+1) % 5 == 0 and (i+1) % 3 != 0:
                tmp = 'Buzz'
            elif (i+1) % 5 == 0 and (i+1) % 3 == 0:
                tmp = 'FizzBuzz'
            arr.append(tmp)
        return arr

sol = Solution()
print(sol.fizzBuzz(15))
