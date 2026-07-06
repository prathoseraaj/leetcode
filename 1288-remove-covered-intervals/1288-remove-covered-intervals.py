class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: (x[0], -x[1]))
        answer = 0
        max_end = 0

        for  interval in intervals:
            if interval[1] > max_end:
                answer +=1
                max_end = interval[1]
        

        return answer