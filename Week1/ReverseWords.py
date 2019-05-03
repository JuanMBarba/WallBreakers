class Solution:
    def reverseWords(self, s: str) -> str:
        
        result = ""
        
        for x in s.split():
            
            result+=x[::-1]+' '
            
        return result[:-1]
