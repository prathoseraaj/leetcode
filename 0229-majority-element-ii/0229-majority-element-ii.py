class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count1, count2 = 0,0
        canditate1, canditate2 = None, None

        for num in nums:
            if canditate1 == num:
                count1 +=1
            
            elif canditate2 == num:
                count2 +=1
            
            elif count1 == 0:
                canditate1, count1 = num, 1
            
            elif count2 == 0:
                canditate2, count2 = num, 1
            
            else:
                count1 -=1
                count2 -=1
        
        result = []
        for c in (canditate1, canditate2):
            if c is not None and nums.count(c) > len(nums)//3:
                result.append(c)

        return result     
        