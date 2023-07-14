# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # def printNodes(headNode):
        #     print("[", end = "")
        #     while headNode:
        #         print(str(headNode.val), end = ", ")
        #         headNode = headNode.next
        #     print("]")

        if head == None or head.next == None:
            return head
        
        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            # printNodes(cur)
            # print("index:", index, "Last:")
            # printNodes(last)
            odd.next = even.next #skip even node
            odd = odd.next

            even.next = odd.next #skip odd node
            even = even.next
        odd.next = evenHead
        return head

