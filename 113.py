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

from typing import List
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        r = []
        path = []
        def helper(node, s):
            print('================================')
            print('node', node)
            print('path', path)
            print('s', s)
            if node.left == None and node.right == None and s - node.val==0:
                print('get get get get get')
                path.append(node.val)
                r.append(path[:])
                path.pop()
            if node.left:
                path.append(node.val)
                helper(node.left, s-node.val)
                path.pop()
            if node.right:
                path.append(node.val)
                helper(node.right, s-node.val)
                path.pop()
        helper(root, sum)
        return r

if __name__ == '__main__':
    l = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    node = TreeNode(l[0])
    node.build(l)
    print('node', node)
    print('left', node.left.left.left.left)
    r = Solution().pathSum(node, 22)
    print('result', r)