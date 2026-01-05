class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        seen = set()
        repeat = 0
        missing = 0

        for num in nums:
            if num in seen:
                repeat = num
                break
            seen.add(num)
        
        n = len(nums)
        expected_sum = (n*(n+1)) // 2
        actual_sum = sum(nums)
        missing = expected_sum - actual_sum + repeat


        return [repeat,missing]
        

        