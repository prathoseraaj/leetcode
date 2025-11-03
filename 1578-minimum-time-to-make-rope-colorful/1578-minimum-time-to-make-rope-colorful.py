class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        answer = 0
        max_time = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # remove the smaller one
                answer += min(max_time, neededTime[i])
                # keep the larger one
                max_time = max(max_time, neededTime[i])
            else:
                max_time = neededTime[i]

        return answer
