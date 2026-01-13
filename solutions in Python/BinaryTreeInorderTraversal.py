class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        i = 0
        stack = [0]
        currentInteration = []
        
        for j in range(len(root)):
            if root[(2 * i) + 1]:
                i = (2 * i) + 1
                stack.append(i)
            elif root[(2 * i) + 2]:
                currentInteration.append(root[i])
                root[i] = None
                stack.pop()

                i = (2 * i) + 2
                stack.append(i)
            else:
                currentInteration.append(root[i])

                root[i] = None
                stack.pop()

        
        return currentInteration
    

practice = Solution()

root = [1,2,3,4,5,None,8,None,None,6,7,9]
print(practice.inorderTraversal(root))