class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(number:int)->int:
            for digit in str(number):
                if digit == '0' or number%int(digit)!=0:
                    return False
            return True
        
        result = []
        
        for integer in range(left, right+1):
            if isSelfDividing(integer):
                result.append(integer)
                
        return result
