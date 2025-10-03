class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort() #sorting the numbers

        closest = float("-inf")
        
        for i in range(len(nums)-2):

            l,r  = i+1,len(nums)-1

            while l <  r:


                curr_sum = nums[i] + nums[l] + nums[r]

                if curr_sum == target:
                    return curr_sum
                
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum
                
                if curr_sum > target:
                    r = r-1
                
                else:
                    l = l+1
        
        return closest