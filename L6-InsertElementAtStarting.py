class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
l=LinkedList()
n=int(input("Enter how many numbers you want to prepend "))
for i in range(n):
    data=int(input("enter data item: "))
    l.prepend(data)
l.print_list()
