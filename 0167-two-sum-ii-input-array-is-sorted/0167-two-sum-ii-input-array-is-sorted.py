class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        freq = {}

        for i,n in enumerate(numbers):
            diff = target - n
            if diff in freq:
                return [freq[diff]+1,i+1]
            freq[n] = i
        

        