"""
Given an integer array `nums`, this function determines if any value appears at least twice in the array.
It returns `True` if any value appears more than once, and `False` if every element is distinct.

Parameters:
    nums (List[int]): A list of integers to check for duplicates.

Returns:
    bool: `True` if duplicates are found, otherwise `False`.

LeetCode Question: Contains Duplicate
"""

# Solution using a set to track seen numbers
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Intuition:
# Using a set allows us to efficiently check for duplicates as sets do not allow duplicate values.

# Time Complexity: O(n), where n is the number of elements in nums.
#Space Complexity: O(n), in the worst case, where all elements are unique and stored in the set.

# Example usage:

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(contains_duplicate(nums))  # Output: False

    nums = [1, 2, 3, 1]
    print(contains_duplicate(nums))  # Output: True