'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() # hash set to track visited nodes
        cur = head

        while cur:
            if cur in seen:
                return True # cycle is detected if we visit node again
            seen.add(cur) # add cur node to seen nodes
            cur = cur.next # update pointer
        return False # cur reaches None, no cycle detected
    
# Intuition:
# The algorithm uses a hash set to track the nodes that have been visited. If we encounter a node that has already been seen, it indicates a cycle in the linked list. If we reach the end of the list (cur becomes None), it means there is no cycle.

# Tortoise and Hare Approach:
# Alternatively, we can use the Tortoise and Hare approach, where two pointers traverse the list at different speeds. If there is a cycle, the two pointers will eventually meet; if there is no cycle, one pointer will reach the end of the list.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head # same pos starting

        while fast and fast.next: # fast.next also has to exist
            slow = slow.next # slow moves by 1
            fast = fast.next.next # fast moves by 2 
            if slow == fast: # they will catch up if a cycle exists
                return True
        return False
    
# The distance between the two pointers will decrease by 1 each time they move, and if there is a cycle, they will eventually meet. 
# If there is no cycle, the fast pointer will reach the end of the list.