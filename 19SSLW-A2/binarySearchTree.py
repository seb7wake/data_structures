class BinarySearchTree:

    COUNT = [10]

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    #insertv node into tree
    def insert(self, root, item):
        if (item < root.val):
            if (root.left != None):
                #call insert function using left node
                BinarySearchTree.insert(self, root.left, item)
            else:
                #save node in tree
                root.left = BinarySearchTree(item)
        else:
            if (root.right != None):
                #call insert function using right node
                BinarySearchTree.insert(self, root.right, item)
            else:
                #save node in tree
                root.right = BinarySearchTree(item)

    #get height of a single node
    def getHeight(self, Node):
        if Node is None or (Node.left is None and Node.right is None): 
            return 0
        else:
            # compute the height of each subself 
            lHeight = BinarySearchTree.getHeight(self, Node.left) 
            rHeight = BinarySearchTree.getHeight(self, Node.right)
            # use the larger one 
            if (lHeight > rHeight): 
                return (lHeight + 1) 
            else:
                return (rHeight + 1) 

    #get sum of heights for every node in the tree
    def getTotalHeight(self, root):
        if (root == None):
            return 0
        res = 0
        return (BinarySearchTree.getTotalHeight(self, root.left) +
                BinarySearchTree.getHeight(self, root) +
                BinarySearchTree.getTotalHeight(self, root.right))
        # nodes = BinarySearchTree.postorderTraversal(self, root)
        # for node in nodes:
        #     res += BinarySearchTree.getHeight(self, node)
        # return res
            

    def getWeightBalanceFactor(self, root):
        weights = []
        if root is None:
            return 0
        else:
            #get a list of nodes in the tree to loop through
            nodes = BinarySearchTree.postorderTraversal(self, root)
            for i in range(len(nodes)):
                #getting heigt of left and right subtree and comparing them
                rh = BinarySearchTree.getHeight(self, nodes[i].right)
                lh = BinarySearchTree.getHeight(self, nodes[i].left)
                weights.append(abs(lh - rh))
            return max(weights)
    
    #traversal through the tree and return array of nodes in tree
    def postorderTraversal(self, root):
        res = []
        if root:
            res = BinarySearchTree.postorderTraversal(self, root.left)
            res = res + BinarySearchTree.postorderTraversal(self, root.right)
            res.append(root)
        return res

    def print2DUtil(self, root, space) : 
        # Base case  
        if (root == None) : 
            return
        # Increase distance between levels  
        space += BinarySearchTree.COUNT[0] 
        # Process right child first  
        BinarySearchTree.print2DUtil(self, root.right, space)  
        # Print current node after space  
        # count  
        print()  
        for i in range(BinarySearchTree.COUNT[0], space): 
            print(end = " ")  
        print(root.val)  
        # Process left child  
        BinarySearchTree.print2DUtil(self, root.left, space)  
  
    # Wrapper over print2DUtil()  
    def print2D(self, root) : 
        
        # space=[0] 
        # Pass initial space count as 0  
        BinarySearchTree.print2DUtil(self, root, 0)  
    
# Driver Code  
if __name__ == '__main__': 
    bst = BinarySearchTree(1)
    bst.insert(bst, 2)
    bst.insert(bst, 3)
    bst.insert(bst, 4)
    bst.insert(bst, 5)
    bst.insert(bst, 6)
    bst.insert(bst, 7)
    bst.insert(bst, 8)
    bst.insert(bst, 0)
    print(bst.getHeight(bst.left))
    print(bst.getTotalHeight(bst))
    print(bst.getWeightBalanceFactor(bst))
    bst.print2D(bst) 