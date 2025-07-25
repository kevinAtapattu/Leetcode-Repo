'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0 
        r = len(nums) - 1
        
        while l < r:
            summ = nums[l] + nums[r]
            if summ == target:
                return [l+1, r+1]
            elif summ < target:
                l += 1
            else:
                r -= 1
            
    
'''
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''

# Intuition:
# we use two pointers, one starting at the beginning (l) and one at the end (r) of the sorted array.
# We calculate the sum of the elements at these two pointers.
# If the sum is equal to the target, we return the indices (adjusted for 1-based indexing).
# If the sum is less than the target, we move the left pointer to the right (l += 1) to increase the sum.
# If the sum is greater than the target, we move the right pointer to the left (r -= 1) to decrease the sum.
# This process continues until we find the two indices that sum to the target.

# time complexity: O(n), where n is the length of the input array. Each element is processed at most once.
# space complexity: O(1), as we are using only a constant amount of extra space