class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0
        total = sum(nums)
        
        for i in range(len(nums)):
            r = total - l - nums[i]
            if l == r:
                return i
            l += nums[i]

        return -1

            
        