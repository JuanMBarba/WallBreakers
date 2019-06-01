class Solution:
    #self.memo = {}
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if target <= 0:
            return[]
        
        result = []
        for index, x in enumerate(candidates):
            if x < target:
                result += [[x] + c for c in self.combinationSum(candidates[index:], target-x)]
            if x == target:
                result.append([x])
        
        return result
            
