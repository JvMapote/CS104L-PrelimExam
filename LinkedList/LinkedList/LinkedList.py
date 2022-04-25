class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_list:
	def __init__(self):
		self.head=node()

	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	
	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total 

	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:
			cur_node=cur_node.next
			elems.append(cur_node.data)
		print(elems)

	def insert(self,index,data):
		if index>=self.length() or index<0:
			return self.append(data)
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				new_node=node(data)
				prior_node.next=new_node
				new_node.next=cur_node
				return
			prior_node=cur_node
			cur_idx+=1

my_list = linked_list()
my_list.append("Dog")
my_list.append("Cat")
my_list.append("Rabbit")
my_list.append("Snake")
my_list.display()
my_list.insert(0,"Bird")
my_list.display()
my_list.insert(3,"Elephant")
my_list.display()

