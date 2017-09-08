class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 1
        buff_dict = {}
        for i, j in enumerate(nums):
            buff_dict[j] = i
        i = 1
        while True:
            if i not in buff_dict:
                return i
            i += 1

sol = Solution()
print(sol.firstMissingPositive([1, 2, 3, 5, -2]))

