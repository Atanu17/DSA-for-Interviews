"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
#Another solution

class Solution2:
    def lengthOfLongestSubstring2(self, s: str) -> int:
        charSet = set()
        l, r, res = 0, 0, 0

        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                r += 1
            else:
                charSet.remove(s[l])
                l += 1
            res = max(res, r - l)
        return res