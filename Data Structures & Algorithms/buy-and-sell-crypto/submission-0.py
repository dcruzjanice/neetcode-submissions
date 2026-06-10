class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        min_price = float("inf")
        max_profit = 0

        for price in prices:
            # update the lowest price
            min_price = min(price, min_price)

            # calculate profit if selling today
            profit = price - min_price

            # update best profit
            max_profit = max(profit, max_profit)

        return max_profit