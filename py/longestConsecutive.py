class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        buff_dict = {}
        res = 0
        for i in nums:
            if i in buff_dict:
                continue
            else:
                left, right = 0, 0
                if i-1 in buff_dict:
                    left = buff_dict[i-1]
                if i+1 in buff_dict:
                    right = buff_dict[i+1]
                longest = left + right + 1
                buff_dict[i] = longest
                buff_dict[i-left] = longest
                buff_dict[i+right] = longest
                res = max(res, longest)
        print(buff_dict)
        return res

sol = Solution()
nums = [[1,2,3],[4,5,6],[7,8,9]]
new = [1,2,3,4,5,6,7,8,9]
print(new[::-1])
print(nums[::-1])

