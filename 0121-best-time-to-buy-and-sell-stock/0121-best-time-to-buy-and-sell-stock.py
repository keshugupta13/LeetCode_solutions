class Solution(object):
    def maxProfit(self, prices):
        left = 0 
        right = 1 
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                currentProfit = prices[right] - prices[left] 
                max_profit =max(currentProfit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
