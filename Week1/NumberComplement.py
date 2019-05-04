class Solution:
    def findComplement(self, num: int) -> int:
        
        binarynum = bin(num)
        
        binarynum =''.join("1" if x == "0" else "0" for x in binarynum[2:])
        
        return int(binarynum, 2)
