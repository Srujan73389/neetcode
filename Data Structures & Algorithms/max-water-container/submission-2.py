class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,h=0,len(heights)-1
        maxi=0
        while l<h:
            total=(h-l)*min(heights[l],heights[h])
            maxi=max(maxi,total)
            if heights[l]<heights[h]:
                l+=1
            else:
                h-=1
        return maxi
        