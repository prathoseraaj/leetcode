class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        res = len(nums)*[0]

        left = 0
        right = len(nums)-1
        pos = len(nums)-1

        while left <= right:
            l = nums[left]**2
            r = nums[right]**2

            if l > r:
                res[pos] = l
                left +=1
            else:
                res[pos] = r
                right -=1
            pos -=1
        
        return res
        