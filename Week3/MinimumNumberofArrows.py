class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if points == []:
            return 0
        
        sPoints = sorted(points, key = lambda x : x[1])
        
        arrows = 1
        
        endP = sPoints[0][1]
        
        for x in sPoints[1:]:
            if endP < x[0]:
                arrows+=1
                endP = x[1]    
        
        return arrows
