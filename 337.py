# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from my_utils import TreeNode
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dp(cur):
            if cur is None: return [0 ,0]
            l = dp(cur.left)
            r = dp(cur.right)
            return [max(l) + max(r), cur.val + l[0] + r[0]]
        return max(dp(root))

if __name__ == "__main__":
    l = [2, 1, 10, 2, 2, 3, 4]
    node = TreeNode(l[0])
    node.build(l)
    print(node)

    r = Solution().rob(node)
    print(r)