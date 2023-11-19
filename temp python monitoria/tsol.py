from tavl import AVL_Tree

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
			if len(myTree.l1)==0:
				myTree.preOrder(root)
			print(myTree.l1)
		if var[1][0:-1]=="INORDEM":
			if len(myTree.l2)==0:
				myTree.inOrder(root)
			print(myTree.l2)
		if var[1][0:-1]=="POSORDEM":
			if len(myTree.l3)==0:
				myTree.posOrder(root)
			print(myTree.l3)
	if var[0]=="REMOVE":
		num = var[1]
		root = myTree.delete(root, num)
	if var[0]=="NIVEL":
		num = var[1]
		val = myTree.getAltura(root)
		try:
			num = myTree.dicio[int(var[1])]
			print(f"Nivel de {var[1]}:", num)
		except:
			print(f"Valor",var[1],"inexistente")
	if var[0]=="ORDEM":
		lista = len(myTree.l2)
		if lista == 0:
			myTree.inOrder(root)
		try:
			num = int(myTree.l2.index(int(var[1])))+1
			print(f"Ordem de {var[1]}:", num)
		except:
			print(f"Valor",var[1],"inexistente")


file1.close()
file2.close()
