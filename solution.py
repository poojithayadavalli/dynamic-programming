class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def linkedList(llist):
    if len(llist)==0:
        return None
    head1=head=ListNode(llist[0])
    for i in range(1,len(llist)):
        head.next=ListNode(llist(i))
        head=head.next
    head.next=None
    return head1

def binaryTree(arr, root, i, n):
    if i < n: 
        temp = TreeNode(arr[i])  
        root = temp 
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n) 
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root
    
def isSubPath(head, root) :
    target = ""
    while head:
        target = target + str(head.val)
        head = head.next
        
    
    def dfs(root, path):
        if target in path:
            return True
            
        if root.left:
            ans =  dfs(root.left, path + str(root.left.val))
            if ans == True:
                return True
                
        if root.right:
            ans  = dfs(root.right, path + str(root.right.val))
            if ans == True:
                return True
        
        return False
        
            
    return dfs(root, str(root.val))
    
tree = input.split(',')
llist= input().split(',')
head = linkedList(llist)
root1=None
root=binaryTree(tree, root1,0,len(tree))
print(isSubPath(header,root))
