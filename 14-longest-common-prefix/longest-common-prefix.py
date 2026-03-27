class Solution(object):
    def longestCommonPrefix(self, s):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not s:
            return ""
        ans=[]
        s.sort()
        first=s[0]
        last=s[-1]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return "".join(ans)
            ans.append(first[i])
        return"".join(ans)        