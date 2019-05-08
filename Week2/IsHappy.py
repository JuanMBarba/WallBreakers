class Solution:
    def isHappy(self, n: int) -> bool:
        
        endless = set()
        
        currentNum = n
        
        while True:
            
            if currentNum == 1:
                return True
            elif currentNum in endless:
                return False
            else:
                endless.add(currentNum)
            
            tempNum = 0
            
            for digit in str(currentNum):
                tempNum+= int(digit)**2
            
            currentNum = tempNum
