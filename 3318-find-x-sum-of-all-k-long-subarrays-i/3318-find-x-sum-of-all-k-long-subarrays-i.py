class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []

        for i in range(n - k + 1):
            window = nums[i:i+k]
            freq = Counter(window)

            # Sort by (frequency desc, value desc)
            sorted_items = sorted(freq.items(), key=lambda y: (-y[1], -y[0]))

            # Take top x elements
            top_x = sorted_items[:x]

            # Sum based on occurrences
            total = sum(num * count for num, count in top_x)
            answer.append(total)

        return answer
        