class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        odd1=""
        even1=""
        odd2=""
        even2=""
        for i in range(len(s1)):
            if i%2==0:
                even1+=s1[i]
            else:
                odd1+=s1[i]
        for i in range(len(s2)):
            if i%2==0:
                even2+=s2[i]
            else:
                odd2+=s2[i]
        odd1=sorted(odd1)
        even1=sorted(even1)
        odd2=sorted(odd2)
        even2=sorted(even2)
        
        if even1==even2 and odd1==odd2:
            return True
        else:
            return False
        