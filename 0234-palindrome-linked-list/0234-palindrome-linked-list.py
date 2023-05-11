# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        q = collections.deque()
        
        if not head:
            return True
        
        node = head
        
        # change to python list
        while node is not None:
            q.append(node.val)
            node = node.next
        
        # check if it's palindrome
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True