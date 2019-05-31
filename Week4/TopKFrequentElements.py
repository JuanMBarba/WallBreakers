class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        
        counter = Counter(nums)
        
        return heapq.nlargest(k, counter.keys(), key = lambda x : counter[x])
