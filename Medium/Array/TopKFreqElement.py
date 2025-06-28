'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}                                  # dictionary to count occurrences of each number
        freq = [[]for i in range(len(nums) + 1)]    # list of lists to store numbers by their frequency

        # for number in nums, the value of key n in count, add 1 to current amount, default 0 if n doesn't exist
        for n in nums:                              # counting how many times a number occurs in nums
            count[n] = 1 + count.get(n, 0)          # 1 + count of number, 0 if doesnt exist

        
        for n, c in count.items():                  # going through every value we counted
            freq[c].append(n)                       # n occurs c amount of times
        
        res = []    
        for i in range(len(freq) - 1, 0, -1):       # iterating in descending order (most frequent first)
            for n in freq[i]:                       # going through every number that occurs i times
                res.append(n)   
                if len(res) == k:
                    return res
    
"""
Visualization of how 'count' updates through every iteration:
    nums = [1, 1, 1, 2, 2, 3]
    Iteration 1: n = 1, count = {1: 1}
    Iteration 2: n = 1, count = {1: 2}
    Iteration 3: n = 1, count = {1: 3}
    Iteration 4: n = 2, count = {1: 3, 2: 1}
    Iteration 5: n = 2, count = {1: 3, 2: 2}
    Iteration 6: n = 3, count = {1: 3, 2: 2, 3: 1}
"""

"""
Visualization of how 'freq' updates through every iteration:
    After building count: {1: 3, 2: 2, 3: 1}
    Initial freq: [[], [], [], [], [], [], []]  # len(nums) + 1 = 7

    Iteration 1: n = 1, c = 3
        freq = [[], [], [], [1], [], [], []]
    Iteration 2: n = 2, c = 2
        freq = [[], [], [2], [1], [], [], []]
    Iteration 3: n = 3, c = 1
        freq = [[], [3], [2], [1], [], [], []]
"""