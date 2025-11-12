# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        # recursive - only checking where we find the start of the subtree
        return (self.isSubtree(root.right, subRoot) or 
        self.isSubtree(root.left, subRoot))

    # helper func - once start of subtree is found, this func compares each element
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.right, subRoot.right) and 
            self.sameTree(root.left, subRoot.left))
        
        return False

        
        
