# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        layers = []
        def parse_layer(nodes):
            next_layer = []
            layer_val = ''
            for node in nodes:
                if node is None:
                    layer_val += 'N '
                    continue
                layer_val += str(node.val)
                layer_val += ' '
                next_layer.append(node.left)
                next_layer.append(node.right)
            layers.append(layer_val)
            return next_layer

        nodes = [self]
        while nodes:
            nodes = parse_layer(nodes)

        p = ''
        for layer in layers[:-1]:
            p += layer
            p += '\n'
        return p
        

    def build(self, l):
        def add_leaf(node, i):
            if len(l) > i + 1 and l[i+1]:
                node.left = TreeNode(l[i+1]) 
            if len(l) > i + 2 and l[i+2]:
                node.right = TreeNode(l[i+2]) 
            return node.left, node.right, i + 2

        def add_layer(nodes, i):
            next_layer = []
            for node in nodes:
                left, right, i = add_leaf(node, i)
                if left: next_layer.append(left)
                if right: next_layer.append(right)
            return next_layer, i

        nodes = [self]
        i = 0
        while i < len(l):
            nodes, i = add_layer(nodes, i)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def helper(s, node):
            s += node.val
            print('--------------------------------')
            print(s, sum, node.val)
            print('left:', node.left)
            print('right:', node.right)
            if node.left is None and node.right is None and s == sum:
                return True
            else:
                if node.left:
                    if helper(s, node.left): return True
                if node.right:
                    if helper(s, node.right): return True
        return helper(0, root)

if __name__ == "__main__":
    node_list = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    s = 22
    node = TreeNode(node_list[0])
    node.build(node_list)
    print(node)
    r = Solution().hasPathSum(node, s)
    print(r)



        #       5
        #      / \
        #     4   8
        #    /   / \
        #   11  13  4
        #  /  \      \
        # 7    2      1
