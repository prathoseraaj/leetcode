class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        doubled = s + s
        check = doubled[1:-1]

        return s in check
        