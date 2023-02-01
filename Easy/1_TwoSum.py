"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

"""
We use a hashmap. We iterate through each element in the array and check if the difference of the target and that element is present in the array. If not then the element and its index is added to the hashmap.
"""

from typing import List


class Solution:
    def twoSum(self,nums: List[int],target: int) -> List[int]:
        prevMap = {} # val : index
        
        for i,n in enumerate(nums):#i and n, index and element
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return    