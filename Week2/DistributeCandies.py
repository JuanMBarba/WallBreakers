class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        halfCandies = len(candies)/2
        uniqueCandies = len(set(candies))
        
        if uniqueCandies - halfCandies >= 0:
            return int(halfCandies)
        else:
            return uniqueCandies
