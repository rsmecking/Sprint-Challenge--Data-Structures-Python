from queue import Queue
from stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):        
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            else:    
                # Repeat the process on the left subtree
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value > self.value:
            # If there is no left child, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            else:    
                # Repeat the process on the left subtree
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: if target is less that self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise 
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
      
    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()
                 
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right != None:
            self.right.for_each(fn)
        if self.left != None:
            self.left.for_each(fn)
    # Part 2 -----------------------
        
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):        
        self.queue = Queue()
        self.queue.enqueue(node)
        while len(self.queue) is not 0:
            node = self.queue.dequeue()
            if node.left:
                self.queue.enqueue(node.left)
            if node.right:
                self.queue.enqueue(node.right)
            print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        self.stack = Stack()
        self.stack.push(node)
        # print(self.stack.pop().value)
        while len(self.stack) > 0:
            node = self.stack.pop()
            if node.left:
                self.stack.push(node.left)
            if node.right:
                self.stack.push(node.right)
            print(node.value)
        
                     
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left: 
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()
           

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left: 
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)