#########################################################
# Adding two numbers represented by linked list.  		#
# The numbers are given as:						  		#
#    First List: 1->2->3  // represents number 321		#
#    Second List: 4->5->6 //  represents number 654		#
# Output												#
#    Resultant list: 5->7->9  // represents number 975  #
#                                                 		#
#########################################################


class Node():														#initialising the node 
	def __init__(self, data):
		self.data = data
		self.next = None

class linklist():													
	def __init__(self):
		self.head = None											#initialising the head to be none for the empty linkedlist

	def insert(self, datt):
		current = self.head
		while(current.next != None):
			current = current.next
		current.next = Node(datt)

	def printll(self):												#function to print the nodes of the linked list
		current = self.head
		while(current != None):
			print(current.data)
			current = current.next
		return
	
	def add(self, p, q):											#function to add the linked lists
		x = p.data + q.data
		y = p.next.data + q.next.data
		z = p.next.next.data + q.next.next.data
		cr = 0
		if (x>9):													#to check for carry
			y = y + int(x/10)
			x = x%10

		if (y>9):													#to check for carry
			z = z + int(y/10)
			y = int(y%10)
		if (z>9):													#to check for carry
			cr = cr + int(z/10)
			z = z%10
		return(x,y,z, cr)											

	def reverse(self):												#function to reverse the linked list
		prev = None
		current = self.head
		while(current is not None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev
		
def main():
	a1 = linklist()
	a1.head = Node(7)
	a2 = Node(6)
	a3 = Node(1)
	a1.head.next = a2
	a2.next = a3
	print('The first number in the reversed order is:')
	a1.printll()													#printing the value of the first number
	print('\n')

	b1 = linklist()
	b1.head = Node(4)
	b2 = Node(5)
	b3 = Node(6)
	b1.head.next = b2
	b2.next = b3
	print('The second number in the reversed order is:')
	b1.printll()													#printing the value of the second number
	print('\n')

	
	c1 = linklist()													#creating th linkedlist for the output of the addtion
	x,y,z,cr = c1.add(a1.head, b1.head)

	c1.head = Node(x)
	c2 = Node(y)
	c3 = Node(z)
	c4 = Node(cr)
	c1.head.next = c2
	c2.next = c3
	c3.next = c4
	
	print('The correct output is:')									#printing the final output after the addtion in the reverse order
	c1.reverse()		
	c1.printll()
	print('\n')



if __name__ =="__main__": main()