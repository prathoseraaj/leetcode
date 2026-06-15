class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        freq = {}
        count = 0

        for char in chars:
            freq[char] = freq.get(char,0)+1
        
        for word in words:
            temp = freq.copy()
            valid = True
            for i in word:
                if i not in temp or temp[i]==0:
                    valid = False
                    break
                else:
                    temp[i]-=1
                
            if valid:
                count += len(word)
        
        return count


                
        