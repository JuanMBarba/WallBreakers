class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return list(zip(*A))
        
        '''
        result = []
        Rows = len(A)
        Columns = len(A[0])
        for x in range(Columns):
            tempList=[]
            for y in range(Rows):
                tempList.append(A[y][x])
            result.append(tempList)
        return result
        '''
