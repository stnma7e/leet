class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # we want to find the middle number of the combined array
        # combining sorted arrays is O(n)
        # we only need to combine to the halfway point of the combined array
        # we can probably be smart about this and stop once we know we've reached halfway

        num_elements = len(nums1) + len(nums2)
        midpoint = num_elements // 2
        evenListSize = False
        if num_elements % 2 == 0:
            evenListSize = True

        i1 = i2 = 0
        lastElem = None
        for i in range(num_elements):
            if i1 >= len(nums1):
                nextElem = nums2[i2]
                i2 += 1
            elif i2 >= len(nums2):
                nextElem = nums1[i1]
                i1 += 1
            elif nums1[i1] <= nums2[i2]:
                nextElem = nums1[i1]
                i1 += 1
            else:
                nextElem = nums2[i2]
                i2 += 1

            if not evenListSize and i == midpoint:
                return nextElem
            if evenListSize and i == midpoint:
                return (lastElem + nextElem) / 2

            lastElem = nextElem

