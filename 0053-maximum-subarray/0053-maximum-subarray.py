class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = nums[0]
        curr_max = nums[0]

        for i in nums[1:]:
            curr_max = max(curr_max+i,i)
            max_sum = max(max_sum, curr_max)
        
        return max_sum
        