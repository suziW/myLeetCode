class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodeList = []
        while head.next is not None:
            nodeList.append(head)
            head = head.next
        nodeList.append(head)

        if len(nodeList) == 1:
            nodeList = [None]
        elif n == len(nodeList):
            del nodeList[0]
        else:
            nodeList[-n - 1].next = nodeList[-n].next

        print(nodeList)
        for n in nodeList:
            print(n.val, n.next)
        return nodeList[0]


def makeListNode(l):
    head = ListNode(l[0])
    temp = head
    for i in l[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    return head


def showListNode(head):
    print('showListNode: --------------------------------------')
    while head.next is not None:
        print(head.val)
        head = head.next
    print(head.val)
    print('showListNode done: --------------------------------------')


if __name__ == "__main__":
    l = [1]

    head = makeListNode(l)
    showListNode(head)
    n = 1

    r = Solution().removeNthFromEnd(head, n)
    showListNode(r)
