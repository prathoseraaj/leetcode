class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i = len(s)-1
        answer = 0

        while s[i] == " ":
            i-=1
        
        while i>=0 and s[i] != " ":
            answer +=1
            i-=1
        return answer
            
            

        