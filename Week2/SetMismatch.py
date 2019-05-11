class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter
        n = len(nums)
        
        counterNums = Counter(nums)
        setNums = set(nums)
        setAllNums = set(range(1, n+1))
        
        return [counterNums.most_common(1)[0][0],list(setAllNums-setNums)[0]]
