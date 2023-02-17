class Node:
    def __init__(self, data):
        self.DataValue = data
        self.LeftPointer = -1
        self.RightPointer = -1

BinaryTree = []
NextNode = -1

def CreateTree(NodeData):
    global NextNode
    NextNode = 0
    BinaryTree.append(Node(NodeData))
    NextNode = NextNode + 1


def AttachLeft(NodeData, ParentNode):
    global NextNode
    BinaryTree.append(Node(NodeData))
    BinaryTree[ParentNode].LeftPointer = NextNode
    NextNode = NextNode + 1


def AttachRight(NodeData, ParentNode):
    global NextNode
    BinaryTree.append(Node(NodeData))
    BinaryTree[ParentNode].RightPointer = NextNode
    NextNode = NextNode + 1


def printTreeLeft():
    Index = 0
    while Index != -1:
        print(BinaryTree[Index].DataValue)
        Index = BinaryTree[Index].LeftPointer



CreateTree("Red")
AttachLeft("Blue", 0)
AttachRight("Green", 0)
AttachRight("Black", 2)
AttachLeft("Brown", 2)
AttachLeft("Peach", 3)
AttachLeft("Yellow", 1)
AttachRight("Purple", 1)
AttachLeft("White", 6)
AttachLeft("Pink", 7)
AttachLeft("Grey", 9)
AttachRight("Orange", 9)


printTreeLeft()


# still working on this
def RecursiveData(Index):
    if BinaryTree[Index].LeftPointer == -1 and BinaryTree[Index].RightPointer == -1:
        return BinaryTree[Index].DataValue
    elif BinaryTree[Index].LeftPointer == -1:
        Index = BinaryTree[Index].RightPointer
        RecursiveData[Index]
    else:
        Index = BinaryTree[Index].LeftPointer
        RecursiveData(Index)


print(RecursiveData(0))
