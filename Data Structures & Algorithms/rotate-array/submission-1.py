class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)
        # k=k%n
        # nums[:]=nums[n-k:]+nums[:n-k]

        k=k%len(nums)
        n=len(nums)-1
        l,r=0,n
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        l,r=0,k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
            
        l,r=k,n
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

        