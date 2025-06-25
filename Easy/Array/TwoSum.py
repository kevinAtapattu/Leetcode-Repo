# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []

        prevMap = {} # value : index        # we use dictionary to store previous indices of the numbers that we come across

        for i, n in enumerate(nums):
            diff = target - n               # we calculate the difference between the target and the current number
            if diff in prevMap:             # if the difference is already in the map, we have found the two numbers that add up to the target
                return [prevMap[diff], i]
            prevMap[n] = i                  # we store the current number and its index in the map if difference is not found in previous map
        # If no solution is found, return an empty list
        return
    
    
# Time Complexity: O(n), where n is the number of elements in nums.
# Space Complexity: O(n), for storing the elements in the dictionary.

# Intuition:
# Using a dictionary to store the indices of the elements allows us to find the complement (target - current number) in constant time.
# This approach avoids the need for a nested loop, making it much more efficient than the brute force method.
