class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sumNums = sum(nums)
        
        if sumNums%2 != 0:
            return False
        
        for x in nums:
            if x == sumNums//2:
                return True
            elif x > sumNums//2:
                return False
        
        else:
            target = sumNums//2
            
            def combinationSum(nums, target) -> bool:
        
                if target <= 0:
                    return False
                
                for index, x in enumerate(nums):
                    if x < target:
                        if combinationSum(nums[index+1:], target-x):
                            return True
                    if x == target:
                        return True

                return False
            
            return combinationSum(sorted(nums,reverse=True), target)
