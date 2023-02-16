class Node:
    def __init__(self,data):
        self.__data = data
        self.__leftChild = None
        self.__rightChild = None

    # function to insert in BST
    def insert(self, data):
        # if value is less than the value of the parent node
        if data < self.__data:
            if self.__leftChild:
                # if we still need to move towards the left subtree
                self.__leftChild.insert(data)
            else:
                self.__leftChild = Node(data)
                return
        # if value is greater than the value of the parent node
        else:
            if self.__rightChild:
                # if we still need to move towards the right subtree
                self.__rightChild.insert(data)
            else:
                self.__rightChild = Node(data)
                return

    # function to search in BST
    def search(self, val):
        # if value to be searched is found
        if val == self.__data:
            return str(val) + " is found in the BST"
        # if value is less than the value of the parent node
        elif val < self.__data:
            # if we still need to move towards the left subtree
            if self.__leftChild:
                return self.__leftChild.search(val)   # recursion
            else:
                return str(val) + " is not found in the BST"
        # if value is greater than the value of the parent node
        else:
            # if we still need to move towards the right subtree
            if self.__rightChild:
                return self.__rightChild.search(val)
            else:
                return str(val) + " is not found in the BST"

    # function to print a BST
    def PrintTree(self):
        if self.__leftChild:
            self.__leftChild.PrintTree()
        print(self.__data),
        if self.__rightChild:
            self.__rightChild.PrintTree()


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)


print(root.search(7))
print(root.search(14))
