class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]

        for n in nums[1:]:
            
            if n < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            max_so_far = max(n, n * max_so_far)
            min_so_far = min(n, n * min_so_far)
            
            result = max(result, max_so_far)
        
        return result