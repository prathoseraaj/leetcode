class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_so_for = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            max_so_for = max(num,max_so_for + num )
            max_sum = max(max_sum,max_so_for)
        
        return max_sum
            
        