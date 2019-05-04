class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        binaryX = bin(x)[2:]
        binaryY = bin(y)[2:]
        
        lenBX = len(binaryX)
        lenBY = len(binaryY)
        
        if lenBX > lenBY:
            
            binaryY = (lenBX-lenBY)*"0"+binaryY
        
        elif lenBX < lenBY:
            
            binaryX = (lenBY-lenBX)*"0"+binaryX   
        
        distance = 0
        
        for numX, numY in zip(binaryX, binaryY):
            
            if numX != numY:
                
                distance+=1
        
        return distance
