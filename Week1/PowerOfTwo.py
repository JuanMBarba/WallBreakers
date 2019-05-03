class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n%2==0:
            x=0
            while True:
                x+=1
                if 2**x > n:
                    break
                if 2**x == n:
                    return True
        return False
