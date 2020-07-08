# dynamic-programming #linked list # binary tree

Ravi is solving a challenge in which the question is given as follows :

Given a binary tree and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

Note:
In this context downward path means a path that starts at some node and goes downwards

Constraints:

1 <= node.val <= 100 for each node in the linked list and binary tree.

The given linked list will contain between 1 and 100 nodes.

The given binary tree will contain between 1 and 2500 nodes.

Example 1:

Input:

1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3

4,2,8

Output: 

true

Explanation: Nodes in linkedlist form a subpath in the binary Tree. 

Example 2:

Input:

1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3

1,4,2,6,8

Output: 

false

Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.

Example 3:

Input:

1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3

1,4,2,6

Output: 

true


