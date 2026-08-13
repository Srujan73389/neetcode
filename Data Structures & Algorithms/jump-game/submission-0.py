class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_in=0
        for i in range(len(nums)):
            if i>max_in:
                return False
            max_in=max(max_in,i+nums[i])
        return True
        