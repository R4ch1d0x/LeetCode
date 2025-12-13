class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(1,2**31):
            if i*i > x:
                return i-1
            elif i*i == x:
                return i
        