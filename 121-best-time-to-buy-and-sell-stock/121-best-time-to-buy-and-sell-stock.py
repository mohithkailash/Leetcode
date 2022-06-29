class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_price = prices[0]
        max_profit = 0
        for i in prices:
            least_price = min(least_price,i)
            profit= i - least_price
            max_profit = max(max_profit,profit)
        return max_profit