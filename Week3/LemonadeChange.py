class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        from collections import defaultdict
        
        bank = defaultdict(int)
        
        for bill in bills:
            if bill == 5:
                bank[bill]+=1
            elif bill == 10:
                if bank[5] > 0:
                    bank[bill] += 1
                    bank[5]-=1
                else:
                    return False
            elif bill == 20:
                if bank[5] > 0 and bank[10] > 0:
                    bank[5]-=1
                    bank[10]-=1
                elif bank[5]>=3:
                    bank[5]-=3
                else:
                    return False
        
        return True
                
