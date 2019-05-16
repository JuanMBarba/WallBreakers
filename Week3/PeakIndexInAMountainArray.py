class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        left = 0
        right = len(A)-1
        
        while left<=right:
            middle = (left+right)//2
            if A[middle]>A[middle-1] and A[middle]>A[middle+1]:
                return middle
            elif A[middle]<A[middle+1]:
                left = middle + 1
            elif A[middle]<A[middle - 1]:
                right = middle - 1
