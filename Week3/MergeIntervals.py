class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if intervals == []:
            return []
        
        
        
        intervals.sort(key = lambda x: x[0])
        
        endIndex = 0
        end = intervals[0][1]
        
        tempIntervals = list(intervals)
        
        deleted = []
        
        for index, interval in enumerate(intervals[1:],1):
            
            if end >= interval[0]:

                if end < interval[1]:                
                    end = interval[1]
                    tempIntervals[endIndex][1] = interval[1]

                deleted.append(index)
            
            else:
                endIndex = index
                end = interval[1]
        
        for index in deleted[::-1]:
            del tempIntervals[index]
        
        return tempIntervals
