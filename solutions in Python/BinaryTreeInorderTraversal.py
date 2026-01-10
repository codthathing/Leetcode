class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        stack = []
        i = 0
        
        if (2 * i) + 1:
            currentLeftmostChild = root[(2 * i) + 1]
        else:
            if i == 0:
                currentLeftmostChild = root[i]
            else:
                stack.append(currentLeftmostChild)
                if (i -  1) / 2 != 0:
                    i = (i -  1) / 2
                else:
                    i = (2 * i) + 2
        