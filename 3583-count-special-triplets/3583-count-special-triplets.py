class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        
        from collections import Counter
        right = Counter(nums)
        left = Counter()
        
        ans = 0
        
        for j in range(len(nums)):
            val = nums[j]
            right[val] -= 1
            
            target = 2 * val
            ans += left[target] * right[target]
            ans %= MOD
            
            left[val] += 1
        
        return ans
