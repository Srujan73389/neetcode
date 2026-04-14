class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat=0
        s,e=0,len(people)-1
        while s<=e:
            if people[s]+people[e]<=limit:
                s+=1
                e-=1
                boat+=1
            else:
                boat+=1
                e-=1
        return boat
        