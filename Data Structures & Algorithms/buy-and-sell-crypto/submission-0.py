class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        max_pro=0
        for price in prices[1:]:
            if price<buy:
                buy=price
            else:
                max_pro=max(max_pro,price-buy)
        return max_pro