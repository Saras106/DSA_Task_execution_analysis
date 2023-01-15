"""
Node Class:
    This is responsible for storing task details in the class and can be added to linked list
"""

class Node:
    #Constructor Implementation
    def __init__(self,id_no,starttime,endtime):
        self.next=None
        self.id_no=id_no
        self.starttime=starttime
        self.endtime=endtime
    
    @property
    def id(self):
        return self.id_no
    @property
    def start_time(self):
        return self.starttime
    @property
    def end_time(self):
        return self.endtime    
    
"""
LinkedList Class:
    This is responsible for implementing Linked List for the tasks and is used for implementing
    various aggregate operations.

"""
class LinkedList:
    #Constructor Implementation
    def __init__(self):
        self.head = None
        
    #This method will return the head of the linked list
    def get_list_head(self):
        return self.head
    
    #This method is responsible for inserting node in the linked list 
    #in the beginning or at end based on the flag as insert_at_starting
    def insert_node(self, node:Node, insert_at_starting=0):
        count=1
        current = self.head
        if insert_at_starting == 1:
            node.next = self.head
            self.head = node
        while current:
            if count+1 == insert_at_starting:
                node.next =current.next
                current.next = node
                return
            else:
                count+=1
                current = current.next

    #This method is responsible for printing the linked list nodes
    def print_linked_list(self):
        tmp=self.head
        while(tmp):
            print(tmp.id_no, tmp.starttime, tmp.endtime)
            tmp=tmp.next
    
    #This method is responsible for printing the linked list nodes in reverse order
    def print_in_reverse(self,head):
        tmp=head
        if tmp==None:
            return
        self.print_in_reverse(tmp.next)
        print(tmp.id_no, tmp.starttime, tmp.endtime)