class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        self.result = 0
        self.lenp = len(prices)
        if self.lenp < 2:
            return self.result
        self.lowest = prices[0]
        
        
        
        def maxPro(index):
            if index == self.lenp:
                return
            if prices[index] < self.lowest:
                self.lowest = prices[index]
            if prices[index] - self.lowest > self.result:
                self.result = prices[index] - self.lowest
            maxPro(index+1)
        
        
       
        maxPro(0)
        
        return self.result
