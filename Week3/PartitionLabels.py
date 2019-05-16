class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        result = []
        
        endpoints = {}
        
        for position, letter in enumerate(S):
            endpoints[letter] = position
        
        start = 0
        end = 0
        
        for index, letter in enumerate(S):
            if end < endpoints[letter]:
                end = endpoints[letter]
            if index == end:
                result.append(end-start+1)
                start = end+1
        
        return result
