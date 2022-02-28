# Node class
class Node:
    
	# Function to initialize the node object
	def __init__(self, data = None):
		self.data = data # Assign data
		self.next = None # Initialize
						# next as null

# Linked List class
class LinkedList:
    # Function to initialize the Linked
	# List object
    def __init__(self):
        self.head = None
    # Printing    
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
    # Insering Node At Beginning
    def AtBegining(self,newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

# Code execution starts here
#if __name__=='__main__':
 
    # Start with the empty list
llist = LinkedList()
 
llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second
second.next = third
llist.printList()
llist.AtBegining(999)
print("Insertion at Begining")
llist.printList()