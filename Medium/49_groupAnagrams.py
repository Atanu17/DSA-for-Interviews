"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""
"""IMPORTANT"""
"""
We use a hashmap where the key is the pattern of count of the alphabets and the value is the list of alphabets with that count

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

count[a-z] = 1e, 1a, 1t
             1e, 1a, 1t

Hashmap
key : value
1e, 1a, 1t:["ate","eat","tea"]   
..........

Time complexity O(m.n.26)~O(m.n)
m is the size of the list
n is the size of each word
26 is the size of the count array
"""

"""
Applying sorting would take O(m.nlogn), since m is the size of the list and sorting each string of size n takes nlogn time so we do not use sorting
"""
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> list[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a.....z
            for c in s:
                count[ord(c) - ord("a")] += 1 # count of each string in list
            
            res[tuple(count)].append(s)
            """
            The count may not be present so we declare res as default dict(defaultdict means that if a key is not found in the dictionary, then instead of a KeyError being thrown, a new entry is created. ) to handle the edge case. The index cannnot be a list(list cannot be keys) since they are mutable so we change it into a tuple
            """
        return res.values()
