class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        curMax, maxSoFar = 0, 0
        for i in range(1, len(prices)):
            curMax += prices[i] - prices[i-1]
            curMax = max(0, curMax)
            maxSoFar = max(curMax, maxSoFar)
        return maxSoFar