class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

# دالة مساعدة لإدراج عقدة جديدة مع المفتاح المعطى

def insert(root,node):
	if root is None:
		root = node
	else:
		if root.val < node.val:
			if root.right is None:
				root.right = node
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)




# دالة مساعدة لإجراء عملية التنقل الوسطي
def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)

r = Node(20)

insert(r,Node(30))
insert(r,Node(10))
insert(r,Node(50))
inorder(r)
# اختبار الدوال السابقة
# لننشئ شجرة البحث الثنائية التالية
#	 50
# /	 \
# 30	 70
# / \ / \
# 20 40 60 80

# insert(r,Node(20))
# insert(r,Node(40))
# insert(r,Node(70))
# insert(r,Node(60))
# insert(r,Node(80))

# طباعة نتيجة التنقل الوسطي







