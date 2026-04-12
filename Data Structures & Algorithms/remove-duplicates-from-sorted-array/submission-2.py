class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        init=1
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[init]=nums[i]
                init+=1
        return init
        