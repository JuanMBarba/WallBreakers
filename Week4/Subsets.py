class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if nums == []:
            return [[]]
        else:
            x = self.subsets(nums[1:])
            result = []
            for i in x:
                result.append(i)
                result.append([nums[0]]+i)
            
            return result
