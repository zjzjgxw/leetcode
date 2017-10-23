class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def robHouse(nums):
            pre_two = nums[0]
            pre_one = max(nums[0], nums[1])
            cur_max = max(pre_one, pre_two)
            for i in range(2, len(nums)):
                cur_max = max(nums[i] + pre_two, pre_one)
                pre_two = pre_one
                pre_one = cur_max
            return max(cur_max, pre_one)

        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(robHouse(nums[:-1]), robHouse(nums[1:]))

sol = Solution()
print(sol.rob([12,4,5,6,34,3,2,4]))