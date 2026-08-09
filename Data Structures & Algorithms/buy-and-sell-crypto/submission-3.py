class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        buy = prices[0]
        sell = 1
        while sell < len(prices):
            profit = prices[sell] - buy
            if prices[sell] < buy:
                buy = prices[sell]
            if profit > max:
                max = profit
            sell += 1
        
        return max
        