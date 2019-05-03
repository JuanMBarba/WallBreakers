class Solution:
    def reverseVowels(self, s: str) -> str:
        
        Lposition=0
        Rposition= len(s) - 1
        
        vowels = ('a', 'e', 'i', 'o', 'u')
        
        NS = [*s]
        
        while Lposition < Rposition:
            
            if NS[Lposition].lower() in vowels and NS[Rposition].lower() in vowels:
                
                left = NS[Lposition]
                
                NS[Lposition] = NS[Rposition]
                
                NS[Rposition] = left
                
                Lposition+=1
                Rposition-=1
                
            if NS[Lposition].lower() not in vowels:
                Lposition+=1
                
            if NS[Rposition].lower() not in vowels:
                Rposition-=1
        
        return ''.join(NS)
