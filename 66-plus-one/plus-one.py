class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res= 0
        for n in digits:
            res = res*10 + n
        
        res += 1
        res1 =[int(digit) for digit in str(res)]

        return res1
        