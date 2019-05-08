class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:        
        jewels = set()
        
        total = 0
        
        for jewel in J:
            jewels.add(jewel)
        
        for stone in S:
            if stone in jewels:
                total+=1
        return total
