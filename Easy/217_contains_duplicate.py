"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

"""Brute forcing or sorting has higher time complexities so we use hash map and sacrifice on the space complexity to have a time complexity of O(n)"""
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() 

        for n in nums:
            if n in hashset:
                return True;
            hashset.add(n)
        return False      