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
print(isSubPath(head,root))
