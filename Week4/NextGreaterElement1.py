class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hmap = {}
        
        stack = []
        
        result =[]
        
        for x in nums2:
            while stack and stack[-1]<x:
                hmap[stack.pop()] = x
            stack.append(x)
        
        
        for x in nums1:
            if hmap.get(x) == None:
                result.append(-1)
            else:
                result.append(hmap[x])
        
        return result
