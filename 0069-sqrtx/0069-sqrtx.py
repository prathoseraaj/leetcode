class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
            
        l = 0
        h = x//2
        ans = 1

        while l<=h:
            mid = (l+h)//2
            num = mid * mid

            if num == x:
                return mid
            elif num < x:
                ans = mid
                l = mid+1
            else:
                h = mid-1
        return ans

        