class Solution:
    def hasPathSum(self, root: List[int], targetSum: int) -> bool:

        #base case for no tree
        if not root:
            return false


        if root.left == None and root.right == None:
            #we have reached leaf node
            return root.val == targetSum

        remainingSum = targetSum - root.val

        return self.hasPathSum(root.left, remainingSum) or self.hasPathSum(root.right, remainingSum)