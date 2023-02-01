"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order."""

"""
nums = [1,1,1,2,2,3], k=2
For each value we are going to count the number of occurances
1 -> 3
2 -> 2
3 -> 1
Then the above list of pairs has be sorted in ascending order so that we get the top k elements. Now in the worst case all elements would be distinct and then sorting would take O(nlogn) but we don't need to sort the entire thing since we need the top k frequent elements.

After counting the number of occurances of each value we can use a max heap to store the pairs above and the key of the max heap would be the number of the occurances that is the count and we will pop from the heap exactly k times to get the desired output. 

Building the heap would take O(n) time and popping from heap takes logn, so to pop k times klogn(k<n)


Using heap to solve the problem we can achieve a time complexity of O(klogn).
"""

"""
There is an even better solution  which takes O(n) time and O(n) memory(hashmap to get count of each number), we still need to count the occurances

We use  bucket sort:
In general bucket sort the indices are the numbers and their ocuurance is stored in the values corresponding to them but the indices can be unbounded.

[1,1,1,2,2,100000]

i       0 1 2 ...... 100000
count     3 2 ...... 1

So we use a modified bucket sort:
Index has the count and the value has a list which consists of the items with that particular count. The number of indices == the number of items in input array + 1.

Thus scanning k elements from right we get top k frequent elements.

[1,1,1,2,2,100000]

i(count )   0     1       2     3       4       5       6
values          [100]   [2]    [1]

"""




from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap to store count of each element
        freq = [[] for i in range(len(nums)+1)] # store list of items with the count = index

        for n in nums:
            count[n] = 1 + count.get(n, 0) # get count

        for n, c in count.items(): 
            freq[c].append(n) #get list of items with a specific count

        res = []

        for i in range(len(freq) - 1, 0, -1):#scan from right
            for n in freq[i]:#scan list of numbers with a particular count 
                res.append(n) #append to result set
                if len(res) == k: # check for size of result list
                    return res
