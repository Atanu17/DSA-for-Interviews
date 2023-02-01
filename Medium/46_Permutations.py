"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # base case
        if (len(nums) == 1):
            # return [nums.copy()]
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

"""
1st pass
1 2 3 

2 3
 
3 
 
3 2

2


 RES = [[3,2,1],[2,3,1]]
"""