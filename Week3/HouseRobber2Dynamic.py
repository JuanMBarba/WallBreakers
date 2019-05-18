class Solution(object):
    def rob(self, nums):
        from collections import defaultdict
        memo = defaultdict(lambda: -1)
        lenNums = len(nums)
        
        if lenNums == 0:
            return 0
        elif lenNums == 1:
            return nums[0]
        
        def robHouse(nums):
            
            previous = 0
            current = 0
            maximum = 0
            for index in range(lenNums-1):
                maximum = max(previous + nums[index], current)
                previous = current
                current = maximum
            
            return current
            
        
        
        return max(robHouse(nums[1:]), robHouse(nums[0:-1]))
