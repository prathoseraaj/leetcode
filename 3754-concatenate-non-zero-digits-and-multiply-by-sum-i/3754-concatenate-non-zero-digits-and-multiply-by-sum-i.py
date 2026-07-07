class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        addition = 0    
        n = str(n)
        res = ""

        for number in n:
            if number != "0":
                addition += int(number)
                res += number
        
        if not res:
            return 0
        return int(res)*addition 

        