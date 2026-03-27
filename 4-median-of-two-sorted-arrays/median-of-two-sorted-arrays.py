class Solution(object):
    def findMedianSortedArrays(self, arr1, arr2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1=len(arr1)
        len2=len(arr2)

        if len(arr1)>len(arr2):
            arr1,arr2=arr2,arr1
            len1,len2=len2,len1
            

        left=0
        right=len(arr1)

        while left<=right:
            mid1=(left+right)//2
            mid2=(len1+len2+1)//2-mid1

            l1=arr1[mid1-1] if mid1>0 else float('-inf')
            l2=arr2[mid2-1] if mid2>0 else float('-inf')
            max_left=max(l1,l2)

            r1=arr1[mid1] if mid1<len1 else float('inf')
            r2=arr2[mid2] if mid2<len2 else float('inf')
            min_right=min(r1,r2)

            if l1<=r2 and l2<=r1:
                if (len1+len2)%2==0:
                    return (max_left+min_right)/2.0
                else:
                    return float(max_left)
            elif l1>r2:
                right=mid1-1
            else:
                left=mid1+1
            


            

        