class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            itr = self.head
            while itr.next != None:
                itr = itr.next
            itr.next = node
    
    def delete(self, node):
        print("test")
    
    def printList(self):
        itr = self.head
        while itr != None:
            print(itr.data)
            itr = itr.next



list = LinkedList()

node1 = Node(4)
node2 = Node(5)

list.append(node1)
list.append(node2)

list.printList()