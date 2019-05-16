class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lenNums = len(nums)
        
        left,right = 0, lenNums-1
        
        
        while left<=right:
            middle = (left+right)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
        return -1
