"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sod(num: int):
            sum = 0
            d = 0
            nod = 0
            while num > 0:
                d = num % 10
                sum = sum + d * d
                num = num // 10
                nod += 1
            return sum
        
        visit = set()
        while n not in visit:
            visit.add(n)
            n = sod(n)
            if n == 1:
                return True
        return False