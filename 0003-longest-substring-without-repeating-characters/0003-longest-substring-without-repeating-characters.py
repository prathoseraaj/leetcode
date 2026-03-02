class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        answer = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            answer = max(answer,r-l+1)
        
        return answer
            

