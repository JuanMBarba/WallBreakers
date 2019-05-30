class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {")":"(", "}" : "{", "]": "["}
        stack = []
        for x in s:
            if x in {"(","[","{"}:
                stack.append(x)
            else:
                if not stack or  hmap[x] != stack.pop():
                    return False
        
        if stack:
            return False
        
        return True
