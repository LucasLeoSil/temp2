# Python code to delete a node in AVL tree
# Generic tree node class
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

# AVL tree class which supports insertion,
# deletion operations
class AVL_Tree(object):
	def __init__(self):
		self.l1 = []
		self.l2 = []
		self.l3 = []
		self.dicio = {}



	def insert(self, root, key):
		
		# Step 1 - Perform normal BST
		if not root:
			return TreeNode(key)
		elif key < root.val:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		# Step 2 - Update the height of the 
		# ancestor node
		root.height = 1 + max(self.getHeight(root.left),
						self.getHeight(root.right))

		# Step 3 - Get the balance factor
		balance = self.getBalance(root)

		# Step 4 - If the node is unbalanced,
		# then try out the 4 cases
		# Case 1 - Left Left
		if balance > 1 and key < root.left.val:
			return self.rightRotate(root)

		# Case 2 - Right Right
		if balance < -1 and key > root.right.val:
			return self.leftRotate(root)

		# Case 3 - Left Right
		if balance > 1 and key > root.left.val:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# Case 4 - Right Left
		if balance < -1 and key < root.right.val:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	# Recursive function to delete a node with
	# given key from subtree with given root.
	# It returns root of the modified subtree.
	def delete(self, root, key):

		# Step 1 - Perform standard BST delete
		if not root:
			valor = str("Valor {} inexistente".format(key))
			print(valor)
			return root

		elif key < root.val:
			root.left = self.delete(root.left, key)

		elif key > root.val:
			root.right = self.delete(root.right, key)

		else:
			if root.left is None:
				temp = root.right
				root = None
				return temp

			elif root.right is None:
				temp = root.left
				root = None
				return temp

			temp = self.getMinValueNode(root.right)
			root.val = temp.val
			root.right = self.delete(root.right,
									temp.val)

		# If the tree has only one node,
		# simply return it
		if root is None:
			valor = str("Valor {} inexistente".format(key))
			print(valor)
			return root

		# Step 2 - Update the height of the 
		# ancestor node
		root.height = 1 + max(self.getHeight(root.left),
							self.getHeight(root.right))

		# Step 3 - Get the balance factor
		balance = self.getBalance(root)

		# Step 4 - If the node is unbalanced, 
		# then try out the 4 cases
		# Case 1 - Left Left
		if balance > 1 and self.getBalance(root.left) >= 0:
			return self.rightRotate(root)

		# Case 2 - Right Right
		if balance < -1 and self.getBalance(root.right) <= 0:
			return self.leftRotate(root)

		# Case 3 - Left Right
		if balance > 1 and self.getBalance(root.left) < 0:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# Case 4 - Right Left
		if balance < -1 and self.getBalance(root.right) > 0:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

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

	def getHeight(self, root):
		if not root:
			return 0
		return root.height

	def getBalance(self, root):
		if not root:
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right)

	def getMinValueNode(self, root):
		if root is None or root.left is None:
			return root

		return self.getMinValueNode(root.left)

	def preOrder(self, root):

		if not root:
			return

		self.l1.append(int(root.val[0:-1]))
		self.preOrder(root.left)
		self.preOrder(root.right)
	def inOrder(self, root):

		if not root:
			return

		
		self.inOrder(root.left)
		self.l2.append(int(root.val[0:-1]))
		self.inOrder(root.right)
	def posOrder(self, root):

		if not root:
			return
		
		self.posOrder(root.left)
		self.posOrder(root.right)
		self.l3.append(int(root.val[0:-1]))

	
	def getAltura(self, root):

		if not root:
			return

		if root.val not in self.dicio:
			self.dicio[int(root.val[0:-1])] = root.height
		self.getAltura(root.left)
		self.getAltura(root.right)
	def setL1(self):
		self.l1 = []
		return
	def setL2(self):
		self.l2 = []
		return 
	def setL3(self):
		self.l3 = []
		return

'''----------------------------------------Divisão------------------------------------------------------'''

file1 = open("3.in","r")
file2 = open("3.out","w")
myTree = AVL_Tree()
root = None
for i in file1:
	var = i.split(" ")
	if var[0]=="ADICIONA":
		num = var[1]
		root = myTree.insert(root, num)
	if var[0]=="PRINT":
		if var[1][0:-1]=="PREORDEM":
			myTree.setL1()
			myTree.preOrder(root)
			valor = str(myTree.l1)
			print(valor)
		if var[1][0:-1]=="EMORDEM":
			myTree.setL2()
			myTree.inOrder(root)
			valor = str(myTree.l2)
			print(valor)
		if var[1][0:-1]=="POSORDEM":
			myTree.setL3()
			myTree.posOrder(root)
			valor = str(myTree.l3)
			print(valor)
	if var[0]=="REMOVE":

		num = var[1]
		root = myTree.delete(root, num)
	if var[0]=="NIVEL":
		num = var[1]
		val = myTree.getAltura(root)
		try:
			num = myTree.dicio[int(var[1])]
			valor = str("Nivel de {}: {}".format(var[1], num))
			print(valor)
		except:
			valor = str("Valor {} inexistente".format(var[1]))
			print(valor)
	if var[0]=="ORDEM":
		myTree.setL2()
		myTree.inOrder(root)
		try:
			num = int(myTree.l2.index(int(var[1])))+1
			valor = str("Ordem de {}: {}".format(var[1], num))
			print(valor)
		except:
			valor = str("Valor {} inexistente".format(var[1]))
			print(valor)

file1.close()
file2.close()