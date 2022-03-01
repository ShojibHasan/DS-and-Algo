# link list

class LinkedList:
    def __init__(self,head,tail,size):
        self.head = head
        self.tail = tail
        self.size = size 
    
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail= self.tail.next
    
    def search(self,data):
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
    
    def pop(self,data):
        ...
    
    def length(self,data):
        ...
        
        

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = [5,6,7,8,9]
head = None
prev = None

for ele in a:
    new_node = Node(ele)
    if head is None:
        head = new_node
        prev = new_node
    else:
        prev.next = new_node
        prev = prev.next
    