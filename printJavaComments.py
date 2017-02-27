# Imagine you are given a java sourec file
# Write a python program that prints only the comments

inp  = open("printJavaInput.java").read()
lines = inp.split("\n")
#print(lines[:10])

import re

lst_mult =  re.findall ( '\/\*(.*?)\*\/', inp, re.DOTALL)
for i in range(len(lst_mult)):
    elt = lst_mult[i]
    lst_mult[i] = "/*" + elt + "*/"
    
lst_singles = re.findall ( '\/\/(.*?)\\n', inp, re.DOTALL)
for i in range(len(lst_singles)):
    lst_singles[i] = "//" + lst_singles[i] + "\n"


final = lst_mult + lst_singles
toPrint  = ""
for k in final:
    toPrint += k
print(toPrint)

out  = open('printJavaOutput.java', 'w')
out.write(toPrint)
out.close()

#for i in lines:
#    print(i)




'''
INPUT:
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

OUTPUT:
/**
 * Count the nodes in the binary tree to which root points, and
 * return the answer.  If root is null, the answer is zero.
 */
// The tree is empty.  It contains no nodes.
// Start by counting the root.
// Add the number of nodes
//     in the left subtree.
// Add the number of nodes
//    in the right subtree.
// Return the total.
// end countNodes()
'''

