# In the diameter of the Tree, use the height of the tree as the reference to solve this problem,the brute force will make the TC O(n*n) which will not pass.

#Try calculating the height of the tree,considering every node as the curve point (or root point) through which the path will flow then the max height from the left and the max height from the right the summation of both will give the diameter of the tree.

# height will be calculated as usual,from every recursive call the max height will be returned and we have to keep a global variable which will track the maximum diameter which we have seen so far and then returned the ans as the longest diameter.

# diameter through every node is the sum of "lh + rh".
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=[0]
        def dfs(node):
            if not node:
                return 0
            lh = dfs(node.left)
            rh = dfs(node.right)
            maxi[0]=max(maxi[0],lh+rh)
            return 1+max(lh,rh)
        dfs(root)
        return maxi[0]