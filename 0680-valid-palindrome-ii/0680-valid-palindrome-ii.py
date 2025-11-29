class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPal(s,l,r):
            while l<r:
                if s[r] != s[l]:
                    return False
                l+=1
                r-=1
            return True

        l,r = 0,len(s)-1

        while l < r:
            if s[r]!=s[l]:
                return isPal(s, l + 1, r) or isPal(s, l, r - 1)
            l+=1
            r-=1
        return True



                
        