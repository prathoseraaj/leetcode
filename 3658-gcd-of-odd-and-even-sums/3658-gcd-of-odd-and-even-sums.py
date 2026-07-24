class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        a = 0
        b = 0

        for num in range(1,(n*2) + 1, 2):
            a += num
            b += num+1
        
        while b != 0:
            a,b = b, a % b
        
        return a