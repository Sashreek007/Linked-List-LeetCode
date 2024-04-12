class Node:
    def __init__(self,value):
        self.value= value
        self.next= None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length= 0
    def append(self,value):
        new_node= Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length +=1
    def __str__(self):
        temp_node=self.head
        result= ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node= temp_node.next
        return result
    
    def nth_last(self,n):
        pointer2=self.head
        pointer1=self.head
        for _ in range(n):
            if pointer2 is None:
                return None
            pointer2=pointer2.next
        while pointer2:
            pointer1=pointer1.next
            pointer2=pointer2.next
        return pointer1.value
    
    def partition(self,x):
        current_node=self.head
        self.tail=self.head
        while current_node:
            nxt=current_node.next
            current_node.next=None
            if current_node.value<x:
                current_node.next=self.head
                self.head=current_node
            else:
                self.tail.next=current_node
                self.tail=current_node
            current_node=nxt
            if self.tail.next:
                self.tail.next= None

    
    
new_linked_list= LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(2)
new_linked_list.append(80)
new_linked_list.append(15)
new_linked_list.append(35)
new_linked_list.partition(40)
print(new_linked_list)
print(new_linked_list.nth_last(2))
