class Solution(object):
    def maxArea(self, height):

        l = 0
        r = len(height)-1
        answer = 0

        while l<r:
            area = min(height[l],height[r])* (r-l)

            answer = max(area,answer)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return answer
            

        
        