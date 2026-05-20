class Solution(object):
    def inorderTraversal(self, root):
        res = []
        
        def helper(node):
            if node is None:
                return
            
            helper(node.left)
            res.append(node.val)
            helper(node.right)

        helper(root)
        return res
    

practice = Solution()

root: list[int | None] = [1,2,3,4,5,None,8,None,None,6,7,9]
print(practice.inorderTraversal(root))