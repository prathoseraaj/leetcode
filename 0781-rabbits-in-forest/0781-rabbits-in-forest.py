class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        freq = {}

        for ans in answers:
            freq[ans] = freq.get(ans,0)+1

        answer = 0
        for f in freq:
            group_size  = f + 1
            groups = ceil(freq[f]/group_size)
            answer += groups * group_size

        return answer
        