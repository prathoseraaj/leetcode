class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:

        arr = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
        
        res = ""
        for word in words:
            sum_char = 0
            for ch in word:
                sum_char += weights[ord(ch)-ord('a')]
            
            module = sum_char % 26
            res += arr[module]
        
        return res

                