"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

We use 2 hashmaps fro s and t respectively to store counts of each character in s and t and then we compare them to find whether they are anagrams. The time and space complexities would be O(s+t) since we use two hashmaps and iterate through both of them"""



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {} #hashmaps


        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        """
        if the character doesn't exist in the hashmap then it would throw key does not exist error. To get around that we use get function with a default value 0 in case the character is not present
        """
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True


"""Solution not preferred, just for info"""
from collections import Counter
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        """
        Counter is a data structure in Python(hashmap) which counts things automatically. The last for loop in the above solution is the work that this statement performs.
        """

"""Solution with O(1) space complexity, no extra memory"""
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        """Assuming that sorting takes no extra space and has a time complexity of O(nlogn)"""
