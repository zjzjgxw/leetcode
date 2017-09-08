class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        pre = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[pre]:
                pre += 1
                nums[pre] = nums[i]
        return pre+1

sol = Solution()
print(sol.removeDuplicates([1,1,2,3,4,5]))