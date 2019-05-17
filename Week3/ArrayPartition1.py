class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        resultSum = 0
        
        sortNums = sorted(nums)
        
        for x in range(len(nums)//2):
            resultSum += sortNums[x*2]
            
        return resultSum
