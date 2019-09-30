# 链表

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rr = ListNode(0)
        r = rr
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            carry = s // 10
            r.next = ListNode(s % 10)
            print(x, y, carry, r.next.val)
            
            r = r.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry: 
            print('last carry is: ', carry)
            r.next = ListNode(carry)
        return rr.next

if __name__ == "__main__":
    # 342 + 465 = 807 ===> 7 0 8
    l1 = ListNode(2)
    ll = l1
    ll.next = ListNode(4)
    ll = ll.next
    ll.next = ListNode(3)
    # print('l1:')
    # while l1:
    #     print('>>>>', l1.val)
    #     l1 = l1.next

    l2 = ListNode(5)
    ll = l2
    ll.next = ListNode(6)
    ll = ll.next
    ll.next = ListNode(4)
    # print('l2:')
    # while l2:
    #     print('>>>>', l2.val)
    #     l2 = l2.next



    r = Solution().addTwoNumbers(l1, l2)
    print('r:')
    while r:
        print('>>>>', r.val)
        r = r.next
