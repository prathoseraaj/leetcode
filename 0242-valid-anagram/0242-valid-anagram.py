class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_s = {}
        freq_t = {}

        for sl in s:
            freq_s[sl] = freq_s.get(sl,0)+1
        for tl in t:
            freq_t[tl] = freq_t.get(tl,0)+1
        
        return freq_s == freq_t
