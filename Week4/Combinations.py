class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        if k == 0:
            return [[]]
        
        if n == k:
            return [[i for i in range(1,n+1)]]
        
        result = [[n]+x for x in self.combine(n-1,k-1)]
        
        result += self.combine(n-1,k)
        
        return result
