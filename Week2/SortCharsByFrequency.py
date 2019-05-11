class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        
        counterS = Counter(s)
        
        result = ""
        
        for letter, count in counterS.most_common():
            
            result+= letter*count
            
        return result
