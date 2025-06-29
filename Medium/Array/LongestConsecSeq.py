'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    

# we use a set to store the unique elements of the input array, which allows for O(1) average time complexity for lookups.
# For each number in the set, we check if it is the start of a consecutive sequence by checking if the previous number (num - 1) is not in the set.
# If it is the start of a sequence, we then count the length of the sequence by checking how many consecutive numbers (num + length) are present in the set.
# The maximum length found during this process is returned as the result.

# Time Complexity: O(n), where n is the number of unique elements in the input array. Each element is processed at most once.
# Space Complexity: O(n), as we are using a set to store the unique elements of the input array.