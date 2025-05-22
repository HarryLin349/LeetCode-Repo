class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        l, r = 0, 0
        offset = 0
        while l < m + offset and r < n:
            print (l ,r)
            if (nums1[l] < nums2[r]):
                l += 1
            else:
                nums1.insert(l, nums2[r])
                l += 1
                r += 1
                offset += 1
        while r < n:
            nums1.insert(l, nums2[r])
            l += 1
            r += 1
        print("m+n", m+n)
        nums1[:] = nums1[:m+n]


'''
Optimized Solution
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

'''