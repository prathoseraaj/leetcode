class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(left,right):
            if left >= right:
                return
            
            mid = (right+left)//2

            merge_sort(left,mid)
            merge_sort(mid+1,right)

            merge(left,mid,right)
        
        def merge(left,mid,right):
            
            l = nums[left:mid+1]
            r = nums[mid+1:right+1]

            i = 0
            j = 0
            k = left

            while i<len(l) and j<len(r):
                if l[i] <= r[j]:
                    nums[k] = l[i]
                    i+=1
                else:
                    nums[k]= r[j]
                    j+=1
                k+=1
            
            while i < len(l):
                nums[k] = l[i]
                i+=1
                k+=1
            
            while j < len(r):
                nums[k] = r[j]
                j+=1
                k+=1
        merge_sort(0,len(nums)-1)
        return nums        
        
        

        
