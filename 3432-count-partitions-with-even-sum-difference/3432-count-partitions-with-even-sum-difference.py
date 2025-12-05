class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        answer = 0

        for i in range(len(nums) - 1):  # partition can't be at the last index
            prefix += nums[i]
            left = prefix
            right = total - prefix

            if (left % 2) == (right % 2):
                answer += 1

        return answer
