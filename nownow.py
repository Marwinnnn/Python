#define the node
class Node:
    data = None
    next = None
#creates a linked list of 5 nodes: 5,4,3,2,1
num = 1
head = None #head does not point to any node yet
while(num <=5): #this creates repeatedly a node(5 nodes)
    n_node = Node() #creates a new node
    n_node.data = num #assigns the value of num in the node
    if head == None: #if it is the first node, head points that node
        head = n_node
    else:#if it is not the first node
        n_node.next = head #link the new node to the first node
        head = n_node#head points the new node
    num = num+1 #increment num for the value of the neext node
#display the contents of the nodes
ptr = head
while(ptr !=None):
    print(ptr.data)
    ptr = ptr.next