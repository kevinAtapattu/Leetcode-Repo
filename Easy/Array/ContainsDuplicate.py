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
# Using a set allows us to efficiently check for duplicates as sets do not allow duplicate values.aaa

# Time Complexity: O(n), where n is the number of elements in nums.
#Space Complexity: O(n), in the worst case, where all elements are unique and stored in the set.


# We can also append nums to a set as a set automatically handles duplicates. If the length of the set is less than the length of nums, it means there are duplicates.
def contains_duplicate(nums):
    return len(set(nums)) < len(nums)

# intuition:
# This approach leverages the properties of sets in Python, which do not allow duplicate values.

# Time Complexity: O(n), where n is the number of elements in nums.
# Space Complexity: O(n), for storing the elements in the set.


# Example usage:

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(contains_duplicate(nums))  # Output: False

    nums = [1, 2, 3, 1]
    print(contains_duplicate(nums))  # Output: True