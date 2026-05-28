class Solution(object):
    def numberOfSubstrings(self, s):
        """                                
        :type s: str
        :rtype: int
        """
        freq=[0,0,0]
        left=0
        res=0
        for right in range(len(s)):
            freq[ord(s[right])-ord('a')]+=1
            while freq[0]>0 and freq[1]>0 and freq[2]>0:
                res+=len(s)-right
                freq[ord(s[left])-ord('a')]-=1
                left+=1
        return res
        

