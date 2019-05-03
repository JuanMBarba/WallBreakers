class Solution:
    def titleToNumber(self, s: str) -> int:
        if s == "":
            return 0
        return (26 * self.titleToNumber(s[:-1])) + (ord(s[-1]) - 64)
