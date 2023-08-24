"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

"""

class Solution(object):
    def merge(self, nums1, a, nums2, b):
        #initialze num1
        i = a -1
        #initialize num2
        c = b -1
        #initialize z
        z = a + b -1
        while c >= 0:
            if i >= 0 and nums1[i] > nums2[c]:
                nums1[z] = nums1[i]
                z-=1
                i -=1
            else: 
                nums1[z] = nums2[c]
                z -= 1
                c -=1