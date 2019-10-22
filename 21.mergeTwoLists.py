from ListNode import ListNode, makeListNode, showListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        temp = head
        while True:
            showListNode('head', head)
            showListNode('l1', l1)
            showListNode('l2', l2)

            if l1 is None:
                temp.next = l2
                break
            elif l2 is None:
                temp.next = l1
                break
            else:
                if l1.val > l2.val:
                    temp.next = l2
                    l2 = l2.next
                else:
                    temp.next = l1
                    l1 = l1.next
                temp = temp.next

        return head.next


if __name__ == '__main__':
    l1 = [1, 2, 4]
    h1 = makeListNode(l1)
    showListNode('h1 is:', h1)
    l2 = [1, 3, 4]
    h2 = makeListNode(l2)
    showListNode('h2 is:', h2)

    r = Solution().mergeTwoLists(h1, h2)
    showListNode('r is:', r)