# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases
        if list1 == None and list2 == None:
            return None 
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1.val < list2.val:
            head = list1
            cur1 = list1.next
            cur2 = list2
        else:
            head = list2
            cur1 = list1
            cur2 = list2.next
        returnHead = head
        while cur1 != None or cur2 != None:
            if (cur2 == None) or ((cur1 != None) and (cur1.val < cur2.val)) :
                head.next = cur1
                cur1 = cur1.next
            else:
                head.next = cur2
                cur2 = cur2.next
            head = head.next
        return returnHead

    def mergeTwoListsOptimal(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        if not list1 or not list2:
            return list1 if list1 else list2
        return dummy.next