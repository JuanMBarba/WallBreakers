class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        from collections import defaultdict
        memo = defaultdict(lambda:-1)
        
        def _minDistance(word1, word2):
            if word1 == word2:
                memo[(word1,word2)] =  0
            elif word1 == "":
                memo[(word1,word2)] = len(word2)
            elif word2 == "":
                memo[(word1,word2)] =  len(word1)
            if memo[(word1,word2)] == -1:
                if word1[0] == word2[0]:
                    _minDistance(word1[1:],word2[1:])
                    memo[(word1,word2)] = memo[(word1[1:],word2[1:])]
                else:
                    _minDistance(word1, word2[1:])
                    insert = 1 + memo[(word1, word2[1:])]
                    
                    _minDistance(word1[1:], word2)
                    delete = 1 + memo[(word1[1:], word2)]
                    
                    _minDistance(word1[1:], word2[1:])
                    replace = 1 + memo[(word1[1:], word2[1:])]
                    
                    memo[(word1,word2)] = min(insert,delete,replace)
        
        _minDistance(word1,word2)
        
        return memo[(word1,word2)]
