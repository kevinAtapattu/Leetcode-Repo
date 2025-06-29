'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n -1
        maxArea = 0 

        while l < r:    # iterating until two pointers meet
            w = r - l   
            h = min(height[l], height[r])   # need smallest height
            a = w * h                       # base x width 
            maxArea = max(maxArea, a)       # taking max of cur area or prev maxArea    

            if height[l] < height[r]:       # if left height is smaller we move left to the right
                l += 1 
            else:
                r -= 1                      # otherwise we move right to the left 

        return maxArea                      # return max area at the end 

# The algorithm uses a two-pointer approach, starting from both ends of the height array and moving towards the center.
# At each step, it calculates the area formed by the lines at the two pointers and updates the maximum area found so far.
# The width of the container is determined by the distance between the two pointers, and the height is determined by the shorter of the two lines.
# The algorithm continues until the two pointers meet, ensuring that all possible pairs of lines are considered

# Time Complexity: O(n), where n is the length of the height array. Each element is processed at most once.
# Space Complexity: O(1), as no additional space is used that scales with input size