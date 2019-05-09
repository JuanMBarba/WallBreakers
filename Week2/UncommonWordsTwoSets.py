class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        
        wordsA = set()
        wordsA2 = set()
        wordsB = set()
        wordsB2 = set()
        
        for word in A.split():
            if word in wordsA:
                wordsA2.add(word)
            else:
                wordsA.add(word)
            
            
        for word in B.split():
            if word in wordsB:
                wordsB2.add(word)
            else:
                wordsB.add(word)
        
        return list(((wordsA^wordsB)-wordsA2)-wordsB2)
