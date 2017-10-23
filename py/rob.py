class Solution(object):
    def robOne(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(nums[0]+nums[2], nums[1])
        if len(nums) >= 4:
            after_three_max = nums[len(nums)-1]
            after_two_max = max(after_three_max, nums[len(nums)-2])
            after_one_max = max(nums[len(nums)-3]+after_three_max, after_two_max)
            curMax = 0
            for i in range(len(nums)-4, -1, -1):
                curMax = max(nums[i] + max(after_three_max, after_two_max), after_one_max)
                after_three_max = after_two_max
                after_two_max = after_one_max
                after_one_max = curMax
            return max(curMax, after_one_max)

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        pre_two = nums[0]
        pre_one = max(nums[0], nums[1])
        cur_max = max(pre_one, pre_two)
        for i in range(2, len(nums)):
            cur_max = max(nums[i] + pre_two, pre_one),
            pre_two = pre_one
            pre_one = cur_max
        return max(cur_max, pre_one)

sol = Solution()
print(sol.rob([12,4,5,6,34,3,2,4]))