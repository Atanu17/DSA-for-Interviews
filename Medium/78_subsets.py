"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        subset = []
        def dfs(i): # index of value in original list
            if i >= len(nums):
                res.append(subset.copy()) # we add a copy since the subset is going to change later
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # DECISION NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
