###############################################
# Program to create a linked list, and find   #
# the node with a given value in the linked	  #
# list.										  #
#											  #
##############################################

class Node():									#initialising the node 
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist():
	def __init__(self):		
		self.head = None 						#initialising the head to be none for the empty linkedlist

	def print_linkedList(self):					#function to print the nodes of the linked list
		a = self.head
		while(a !=None):
			print(a.data)
			a = a.next

	def find_a_number(self, value):				#function to search for a given node in the linked list
		temp = self.head
		count = 1
		while(temp.data!=value):
			temp = temp.next
			if(temp==None):
				print('not found')
				return
			else:
				count +=1
		print(count)							#will return the position where the node is found


def main():
    
    z = linkedlist()							#initialising the linkedlist
    z.head = Node(1)							#initialising the first node
    b = Node(2)
    c = Node(3)
    d = Node(4)

    z.head.next = b 							#linking the head with the next node
    b.next = c
    c.next = d
    
    z.print_linkedList()
    print('\n')

    z.find_a_number(3)							#find a node with value 3 in the linkedlist
    

if __name__ =="__main__": main()