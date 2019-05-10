class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        finalGroups = set()
        
        for string in A:
            evenIndex = sorted(string[::2])
            oddIndex = sorted(string[1::2])
            finalGroups.add("".join(evenIndex+oddIndex))
        return len(finalGroups)
