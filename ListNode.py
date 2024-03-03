class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def makeListNode(l):
    head = ListNode(l[0])
    temp = head
    for i in l[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    return head


def showListNode(s, head):
    print(s, end=' ')
    if head is not None:
        while head.next is not None:
            print(head.val, end=',')
            head = head.next
        print(head.val)
    else:
        print('None')