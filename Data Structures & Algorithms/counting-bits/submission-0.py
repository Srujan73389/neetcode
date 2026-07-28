class Solution:
    def countBits(self, n: int) -> List[int]:
        anser=[0]
        for i in range(1,n+1):
            anser.append(anser[i//2]+i%2)
        return anser
        
        