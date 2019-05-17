class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0
        
        if prices == []:
            return result
        
        lowest = prices[0]
        
        for price in prices:
            if price < lowest:
                lowest = price
            if price - lowest > result:
                result = price - lowest
        
        return result
