##################################################
# Program to create a linked list, and reverse   #
# it.                                            #
#               							     #
#											     #
##################################################

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

    def reverse(self):                          #function to reverse the linked list
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


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

    z.reverse()                                 #function to reverse a linked list
    z.print_linkedList()						#printing the linked list after reversing it
    
if __name__ =="__main__": main()
