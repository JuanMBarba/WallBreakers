class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if nums == []:
            return [[]]
        
        result = []
        
        for x in self.permute(nums[1:]):
            for i in range(len(nums)):
                result.append(x[:i] + [nums[0]] + x[i:])
                
        return result
