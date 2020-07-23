#(6) Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = [root]
        leftToRight = True
        while q:
            tmp = []
            cnt = len(q)
            while cnt:
                node = q.pop(0)
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                cnt -= 1
            if leftToRight:
                result.append(tmp)
                leftToRight = False
            else:
                result.append(tmp[::-1])
                leftToRight = True
        return result
