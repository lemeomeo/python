# making a Node class
class Node():
	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node
	
class LinkedList():
	def __init__(self):
		self.head_node = None
	#print statement runs forver if we have a cycle
	def print(self):
		current_node = self.head_node
		while current_node:
			print(current_node.value)
			current_node = current_node.next_node

def detect_cycle(head):
	if head == None: return False
	fast = head.next_node
	slow = head
	while fast != None and slow != None and fast.next_node != None:
		if fast == slow: return True
		fast = fast.next_node.next_node
		slow = slow.next_node
	return False
	
		
# Test Linked list
# 1 -> 2 -> 3 -> 4 -> 5 -> 3 : return True
list = LinkedList()
node1 = Node(1)
list.head_node = node1
node2 = Node(2)
list.head_node.next_node = node2
node3 = Node(3)
list.head_node.next_node.next_node = node3
node4 = Node(4)
list.head_node.next_node.next_node.next_node = node4
node5 = Node(5)
list.head_node.next_node.next_node.next_node.next_node = node5
list.head_node.next_node.next_node.next_node.next_node.next_node = node3
# list.print()

list2 = LinkedList()

# detect cycle
print(detect_cycle(list.head_node))
print(detect_cycle(list2.head_node))


