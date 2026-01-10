# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, target):
            # base case (should never really run, just to cover edge case)
            if not root:
                return False
            # leaf node (should return here)
            if not root.left and not root.right:
                return root.val == target

            hasLeft = dfs(root.left, target - root.val)
            hasRight = dfs(root.right, target - root.val)
            
            return hasLeft or hasRight

        return dfs(root, targetSum)

