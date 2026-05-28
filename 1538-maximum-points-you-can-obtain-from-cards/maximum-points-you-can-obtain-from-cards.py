class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n=len(cardPoints)
        total=sum(cardPoints[:k])
        maxPoints=total
        for i in range(k):
            total-=cardPoints[k-i-1]
            total+=cardPoints[n-i-1]
            maxPoints=max(maxPoints,total)
        return maxPoints