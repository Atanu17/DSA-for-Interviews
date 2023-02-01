"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.
"""
# My implementation
import heapq
from typing import List


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        res = 0
        while k > 0:
            res = heapq.heappop(nums)
            k -= 1
        res = -1 * res
        return res

# Python being python :-)
class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]

# NeetCode implementation using quick-select algorithm
# O(n^2) in worst case but O(n) in average case
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k # index pf kth largest element

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r): # l to r-1 since rth element is the pivot
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p] # swap in one line in python
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k: return quickSelect(l, p - 1)
            elif p < k : return quickSelect(p + 1, r)
            else: return nums[p]
        return quickSelect(0, len(nums) - 1)

