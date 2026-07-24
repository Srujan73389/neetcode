class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        k=k%len(nums)
        
        rotate(0,len(nums)-1)
        rotate(0,k-1)
        rotate(k,len(nums)-1)                
        