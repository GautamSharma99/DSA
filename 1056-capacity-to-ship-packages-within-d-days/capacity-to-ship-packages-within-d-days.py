class Solution(object):
    def daysNeeded(self,weights,capacity):
        day=1
        currentLoad=0
        for w in weights:
            if currentLoad+w > capacity:
                day+=1
                currentLoad=w
            else:
                currentLoad+=w
        return day

    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            needed=self.daysNeeded(weights,mid)
            if needed<=days:
                high=mid
            else:
                low=mid+1
        return low
        