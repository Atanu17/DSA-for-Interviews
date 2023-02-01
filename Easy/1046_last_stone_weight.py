"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
"""
# My implementation
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = stones
        for i in range(len(minHeap)):
            minHeap[i] = minHeap[i] * -1
        heapq.heapify(minHeap)
        
        while len(minHeap) > 1:
            val1 = -1 * heapq.heappop(minHeap)
            val2 = -1 * heapq.heappop(minHeap)
            if not val1 == val2:
                heapq.heappush(minHeap, (-1 * val1) - (-1 * val2))
        if len(minHeap) == 1:
            return -1 * minHeap[0]
        else:
            return 0
# NeetCode implementation
class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        stones.append(0) #stones array empty edge case is handled
        return abs(stones[0])
