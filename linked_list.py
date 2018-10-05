#Program to implement singly linked list
class Node:
     def __init__(self,data):
           self.data=data
           self.next=None

class LinkedList:
      def __init__(self):
          self.head=None

      def printList(self):
           temp=self.head
           while(temp):
               print temp.data,
               temp=temp.next
      
      def push(self,new_data):
           new_node=Node(new_data)
           new_node.next=self.head
           self.head=new_node

      def insert_any(self,data,n):
           new_node=Node(data)
           temp=self.head
           while(temp.data!=n):
                temp=temp.next
           new_node.next=temp.next
           temp.next=new_node

      def insert_last(self,data):
           new_node=Node(data)
           temp=self.head
           while(temp.next):
               temp=temp.next
           temp.next=new_node

      def delete_first(self):
          if self.head==None:
             print("Linked list is empty")
          else:
             self.head=self.head.next

      def delete_last(self):
          if self.head==None:
             print("Linked list is empty")
          else:
             temp=self.head.next
             temp1=self.head
             while(temp.next):
                 temp=temp.next
                 temp1=temp1.next
             temp1.next=None


if __name__=='__main__':
    llist=LinkedList()
    
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)

    llist.head.next=second
    second.next=third
    
    print("Initial Linked List")
    llist.printList()

    print("\nLinked List after insertion at beginning")
    llist.push(23)
    llist.printList()

    print("\nLinked list after insertion after a node")
    llist.insert_any(5,2)
    llist.printList()

    print("\nLinked List after insertion at the end")
    llist.insert_last(6)
    llist.printList()

    print("\nLinked List after deletion of first node")
    llist.delete_first()
    llist.printList()

    print("\nLinked List after deletion of last node")
    llist.delete_last()
    llist.printList()
