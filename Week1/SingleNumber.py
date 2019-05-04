class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        record = {}
        
        for x in nums:
            
            if record.get(x):
                
                record.pop(x)
            
            else:
                
                record[x] = 1
        
        return record.popitem()[0]
