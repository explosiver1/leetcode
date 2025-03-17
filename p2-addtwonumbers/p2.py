#!/python.exe

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1: int = 0
        n2: int = 0
        i: int = 1
        cursor: Optional[ListNode]
        cursor = l1
        n1 = cursor.val
        while (cursor.next is not None):
            cursor = cursor.next
            i = i * 10
            n1 = n1 + (cursor.val * i)
        i = 1
        cursor = l2
        n2 = cursor.val
        while (cursor.next is not None):
            cursor = cursor.next
            i = i * 10
            n2 = n2 + (cursor.val * i)
        n3 = n1 + n2
        l3: Optional[ListNode] = ListNode()
        cursor = l3
        while (n3 > 0):
            cursor.val = n3 % 10
            n3 = n3 // 10
            if (n3 > 0):
                cursor.next = ListNode()
                cursor = cursor.next
        return l3
            
            
            
            
            
            
            
