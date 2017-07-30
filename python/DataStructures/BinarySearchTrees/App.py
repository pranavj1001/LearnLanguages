from BinarySearchTree import BinarySearchTree

newBST = BinarySearchTree()


newBST.insert(12)
newBST.insert(32)
newBST.insert(42)
newBST.insert(90)
newBST.insert(1)
newBST.insert(-2)

print("=====")

newBST.traverseInOrder()

print("=====")

newBST.remove(42)
newBST.traverseInOrder()

print("=====")

print(newBST.getMax())

print("=====")

print(newBST.getMin())

print("=====")

newBST.remove(12)
newBST.traverseInOrder()

print("=====")

newBST.insert(45)

newBST.traverseInOrder()

print("=====")





