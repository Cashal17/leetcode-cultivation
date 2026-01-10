## Takeaways:

The state we update when we pass down to recursive DFS calls for our right and left subtrees is our targetSum - currNode.val because we are looking for a valid path in either right or left subtree, so when we reach the correct leaf node at the end of the correct path, its .val should be equal to the remaining targetSum implying that from the root to that leaf, the path's sum was the targetSum and was therefore valid.

Otherwise, if we reach a null node without a leaf node ending in valid path, then that path is obviously invalid so we propagate False back up.
