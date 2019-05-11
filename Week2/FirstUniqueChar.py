class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        counterS = Counter(s)

        for index,letter in enumerate(s):

            if counterS[letter] == 1:
                return index
        
        return -1
