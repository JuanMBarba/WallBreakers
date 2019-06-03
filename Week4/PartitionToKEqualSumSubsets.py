class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        sumNums = sum(nums)
        
        if sumNums%k != 0:
            return False
        
        target = sumNums//k
        
        if max(nums) > target:
            return False
        if k == 1:
            return True
        else:
            
            pnums = sorted(nums,reverse=True)
            mpnums = list(pnums)
            def combinationSum(nums, target, d, pnums):
                
                if target <= 0:
                    return False
                
                for index, x in enumerate(nums):
                    if x < target:
                        y = combinationSum(nums[index+1:], target-x, d+1+index, pnums)
                        if y:
                            pnums = y
                            pnums = pnums[:index+d]+pnums[index+d+1:]
                            return pnums
                    if x == target:
                        pnums = pnums[:index+d]+pnums[index+1+d:]
                        return pnums

                return False
            
            
            for i in range(len(mpnums)):
                if i > 0:
                    pnums = mpnums[i+1:]+[mpnums[i]]
                    mpnums = list(mpnums)
                count = 0
                while pnums:
                    y = combinationSum(pnums, target, 0, pnums)
                    if y:
                        pnums = y
                        count+=1
                        if count == k-1:
                            return True

                    else:
                        break

            
            return False
