class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 :
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        pre_two_step = 1
        pre_one_step = 2
        all_step = 0
        for i in range(2, n):
            all_step = pre_one_step + pre_two_step
            pre_two_step = pre_one_step
            pre_one_step = all_step
        return all_step

