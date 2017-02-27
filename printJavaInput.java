/**
 * Count the nodes in the binary tree to which root points, and
 * return the answer.  If root is null, the answer is zero.
 */
static int countNodes( TreeNode root ) {
   if ( root == null )
      return 0;  // The tree is empty.  It contains no nodes.
   else {
      int count = 1;   // Start by counting the root.
      count += countNodes(root.left);  // Add the number of nodes
                                       //     in the left subtree.
      count += countNodes(root.right); // Add the number of nodes
                                       //    in the right subtree.
      return count;  // Return the total.
   }
} // end countNodes()