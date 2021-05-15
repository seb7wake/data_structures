class AVLTreeMap:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.left = None 
        self.right = None 
        self.height = 0
    
    def get(self, root, key):
        if not root:
            return None
        elif key < root.key:
            root.left = self.get(root.left, key)
        elif key > root.key:
            root.right = self.get(root.right, key)
        else:
            return root.val
        

    def put(self, root, key, value):
        # Step 1 - Perform normal BST
        if not root:
            return AVLTreeMap(key, value)
        elif key < root.key:
            root.left = self.put(root.left, key, value)
        else:
            root.right = self.put(root.right, key, value)
        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
        # Step 3 - Get the balance factor
        balance = self.getBalance(root)
        # Step 4 - If the node is unbalanced, 
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)
        # Case 2 - Right Right
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)
        # Case 3 - Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    


    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        # Perform rotation
        y.right = z
        z.left = T3
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
        # Return the new root
        return y

    
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        # Perform rotation
        y.left = z
        z.right = T2
        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
        # Return the new root
        return y
    
    def inOrder(self, root): 
        if not root: 
            return
        self.preOrder(root.left) 
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.right) 

if __name__ == '__main__': 
    avl = AVLTreeMap(15, 'bob')
    avl.put(avl, 20, 'anna')
    avl.put(avl, 24, 'tom')
    avl.put(avl, 10, 'david')
    avl.put(avl, 13, 'david')
    avl.put(avl, 7, 'ben')
    avl.put(avl, 30, 'karen')
    avl.put(avl, 36, 'erin')
    avl.put(avl, 25, 'david')
    # print(avl.inOrder(avl))
    print(avl.get(avl, 24))
    print(avl.height)