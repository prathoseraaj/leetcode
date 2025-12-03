class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        res = sum(nums)
        operation = res % k

        return operation