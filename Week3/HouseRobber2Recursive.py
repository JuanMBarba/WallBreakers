class Solution(object):
    def rob(self, nums):
        from collections import defaultdict
        memo = defaultdict(lambda: -1)
        lenNums = len(nums)
        
        if lenNums == 0:
            return 0
        elif lenNums == 1:
            return nums[0]
        
        def robHouse(first,last):
            
            
            if first == last:
                return nums[first]
            
            if first > last:
                return 0
            
            if memo[(first,last)] == -1:
                
                memo[(first,last)] = max(robHouse(first+2, last) + nums[first], robHouse(first+1, last))

            return memo[(first,last)]
        
        
        return max(robHouse(0,lenNums-2), robHouse(1,lenNums-1))
