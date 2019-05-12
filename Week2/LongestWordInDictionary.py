class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        setW = set(words)
    
            
        for word in sorted(sorted(words), key = lambda r: len(r), reverse = True): 
            if len(set([word[:x] for x in range(1,len(word)+1)]).intersection(setW)) == len(word):
                return word
        
        return ""
