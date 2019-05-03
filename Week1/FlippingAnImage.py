class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result=[]
        for item in A:
            item = [abs(num-1) for num in item[::-1]]
            result.append(item)
        return result
