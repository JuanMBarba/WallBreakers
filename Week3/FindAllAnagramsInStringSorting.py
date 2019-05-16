class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        lenP = len(p)
        sP = sorted(p)
        output = []
        index = 0
        last = False
        while index < len(s) - lenP + 1:
            if s[index+lenP-1] not in p:
                index = index+lenP
                last = False
                continue
            if last and s[index+lenP-1] == s[index-1]:
                output.append(index)
                index+=1
                continue
            elif s[index:index+lenP] == p:
                output.append(index)
                last= True
            elif sorted(s[index:index+lenP]) == sP:
                output.append(index)
                last=True
            else:
                last = False
            index+=1
                
        return output
