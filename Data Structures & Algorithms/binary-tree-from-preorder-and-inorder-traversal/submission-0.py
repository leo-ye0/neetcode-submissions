# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        def array_to_tree(left: int, right: int) -> Optional[TreeNode]:
            # Base Case: No elements to construct the tree
            if left > right:
                return None

            # 2. The next element in preorder is ALWAYS the root of current subtree
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            # 3. Find where this root splits the inorder array
            split_idx = inorder_map[root_val]

            # 4. Recursively build left and right children
            # Note: We must build LEFT first because preorder traverses left first
            root.left = array_to_tree(left, split_idx - 1)
            root.right = array_to_tree(split_idx + 1, right)

            return root

        return array_to_tree(0, len(inorder) - 1)