class Solution(object):
    def largestOddNumber(self, s):
        """
        :type num: str
        :rtype: str
        """
        ind=-1
        for i in range(len(s)-1,-1,-1):
            if int(s[i])%2==1:
                ind=i
                break
            while i<ind and s[i]=='0':
                i+=1
        return s[:ind+1]

        