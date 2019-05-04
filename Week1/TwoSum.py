class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictionary = {}
        
        for index, num in enumerate(nums):
            
            complement = target - num
            
            
            
            if type(dictionary.get(complement)) == int:
                
                return [dictionary[complement], index]
            
            dictionary[num] = index
