class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        number = int("".join([str(x) for x in digits]))+1
        return [int(x) for x in str(number)]
