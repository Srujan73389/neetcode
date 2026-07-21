class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l=j+1
                r=len(nums)-1
                while l<r:
                    res=nums[i]+nums[j]+nums[l]+nums[r]
                    if res<target:
                        l+=1
                    elif res>target:
                        r-=1
                    else:
                        triplet=[nums[i],nums[j],nums[l],nums[r]]
                        answer.append(triplet)
                        while l<r and nums[l]==triplet[2]:
                            l+=1
                        while l<r and nums[r]==triplet[3]:
                            r-=1
        return answer
        