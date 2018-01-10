###############################################
# Program to create a linked list, and insert #
# at different positions.					  #
#											  #
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

    def insert_at_mid(self, key, value):		#function to insert the node in the middle of the linked list
    	count = 1								#here ky denotes the position where the node is to be inserted
    	r = self.head
    	while(count!=(key-1)):
    		r = r.next
    		count += 1
    	t = Node(value)
    	t.next = r.next
    	r.next = t

    def insert_at_end(self, value):				#function to insert the node at the end of the linked list
    	temp = self.head
    	while(temp.next!= None):
    		temp = temp.next

    	new_node = Node(value)
    	temp.next = new_node

    def insert_at_first(self,datta):			#function to insert the node at the front of the linked list
    	temp = self.head
    	b = Node(datta)
    	self.head = b
    	b.next = temp


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

    z.insert_at_end(20)							#inserting the node with value 20 at the end of the linked list
    z.print_linkedList()
    print('\n')

    z.insert_at_mid(2,10)						#inserting the node with value 10 at position 2 of the linked list
    z.print_linkedList()
    print('\n')

    z.insert_at_first(30)						#inserting the node with value 30 at the front of the linked list
    z.print_linkedList()
    print('\n')
    

if __name__ =="__main__": main()
    	
    