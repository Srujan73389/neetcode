class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element=0
        counts=0
        for num in nums:
            if counts==0:
                element=num
            if num==element:
                counts+=1
            else:
                counts-=1
        return element
        