class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        a = 1

        while True:
            if a in nums:
                a+=1
            else:
                return a
            