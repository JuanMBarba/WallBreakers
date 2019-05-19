class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        len1= len(word1)
        len2= len(word2)
        memo = [[0]*(len2+1) for x in range(len1+1)]
        
        if len1 == 0:
            return len2
        elif len2 == 0:
            return len1
        
        for x in range(len1+1):
            for y in range(len2+1):  
                if y == 0:
                    memo[x][y] = x
                    
                elif x == 0:
                    memo[x][y] = y
        for x in range(1, len1+1):
            for y in range(1,len2+1):
                if word1[x-1] == word2[y-1]:
                    memo[x][y] = memo[x-1][y-1]
                else:
                    memo[x][y] = 1 + min(memo[x-1][y], memo[x][y-1], memo[x-1][y-1])


        
        return memo[-1][-1]
