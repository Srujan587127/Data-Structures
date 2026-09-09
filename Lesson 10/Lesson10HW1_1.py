class Node:
    def __init__(self,value):
        self.value=value
        self.left = None
        self.right=None



def height(root):
    if root == None:
        return -1    

    lh = height(root.left)   
    rh= height(root.right)  

    if lh>rh:
        ans = lh
    else :
        ans=rh

    return ans+1



root=Node("Root")
root.left = Node("Left")
root.left.left=Node("LeftLeft")


h = height(root)
print("height of tree is:",h)