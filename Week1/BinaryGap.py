class Solution:
    def binaryGap(self, N: int) -> int:
        
        binaryN = bin(N)[2:]
        
        currentGap = 0
        maxGap = 0
        
        for x in binaryN:
            
            if x == "1" and maxGap < currentGap:
                
                maxGap = currentGap
                currentGap = 0

            elif x == "1":
                
                currentGap = 0
                
            currentGap+=1
            
              
        return maxGap
