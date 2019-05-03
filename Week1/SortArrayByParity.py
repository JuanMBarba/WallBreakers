class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result = []
        oddNumbers = []
        for number in A:
            if number%2 == 0:
                result.append(number)
            else:
                oddNumbers.append(number)
        
        result+=oddNumbers

        return result
