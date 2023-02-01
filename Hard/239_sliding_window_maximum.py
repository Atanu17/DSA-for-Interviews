"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""
# Monotonically decreasing queue (dequeue is used)

from typing import List

from matplotlib import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # pop smaller values from right of queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output