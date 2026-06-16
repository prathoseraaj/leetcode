class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(nums,target,leftBias):

            l = 0 
            r = len(nums)-1
            i=-1

            while l <= r:
                m = (l+r)//2

                if nums[m] > target:
                    r -=1
                elif nums[m]< target:
                    l+=1
                
                else:
                    i = m

                    if leftBias:
                        r-=1
                    else:
                        l+=1
            return i
                    
                
        left = binarySearch(nums,target,True)
        right = binarySearch(nums,target,False)

        return [left,right]
