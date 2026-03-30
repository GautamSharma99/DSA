class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        p=0
        for i in s:
            if i=="(":
                p+=1
            elif i==")":
                p-=1
            ans=max(ans,p)
        return ans
        