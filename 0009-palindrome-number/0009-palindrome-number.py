class Solution:
    def isPalindrome(self, x: int) -> bool:

        l = 0
        r = len(str(x))-1

        str_num = str(x)

        while l <= r:
            if str_num[l] == str_num[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        