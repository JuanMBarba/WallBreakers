class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict
        import re
        record = defaultdict(int)
        
        for word in re.split("\W+",paragraph):
            record[word.lower()]+=1
            
        maximum = 0
        word = ""
        for item in record.items():
            if item[0] in banned:
                continue
            if item[1] > maximum:
                maximum = item[1]
                word = item[0]
        
        return word
