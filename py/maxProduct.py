class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 0:
            return 0
        preMax, preMin = nums[0], nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            curMax = max(preMin*nums[i], preMax*nums[i], nums[i])
            curMin = min(preMax*nums[i], preMin*nums[i], nums[i])
            res = max(res, curMax)
            preMax = curMax
            preMin = curMin
        return res
