class Solution(object):
    def BinarySearch(self, nums, value):
        """
        :param nums:
        :param value:
        :return:
        """
        if nums is None:
            return -1
        low, high = 0, len(nums)-1
        mid = (low + high) // 2
        while low <= high:
            if nums[mid] == value:
                return mid
            if nums[mid] < value:
                low = mid + 1
            if nums[mid] > value:
                high = mid - 1
            mid = (low + high) // 2
        return -1

    def InsertionSearch(self, nums, value):
        """
        :param nums:
        :param value:
        :return:
        """
        if nums is None:
            return -1
        low, high = 0, len(nums)-1
        mid = low + int((value - nums[low])/(nums[high] - nums[low])*(high - low))
        while low <= high:
            if nums[mid] == value:
                return mid
            if nums[mid] < value:
                low = mid + 1
            if nums[mid] > value:
                high = mid - 1
            mid = low + int((value - nums[low])/(nums[high] - nums[low]) * (high - low))
        return -1
sol = Solution()
print(sol.BinarySearch([1,4,6,7,10,24,56,60,67,99],1))
print(sol.InsertionSearch([1,4,6,7,10,24,56,60,67,99],25))