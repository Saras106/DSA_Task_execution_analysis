from itertools import count
from src.LinkedList import LinkedList

"""
Aggregate class is responsible for implementating various operations on the linked list
    1. Get Minimum Timed Task Details
    2. Get Maximum Timed Task Details
    3. Get Average of all the execution times of the tasks pushed in the linked list
"""
class Aggregate:
    
    #Initializing linked list object for various operations 
    def __init__(self, linked_list:LinkedList):
        self.linked_list = linked_list
    
    #Function responsible for searching the task having maximum execution time among all the tasks
    def get_maximised_time_task(self):
        tmp=self.linked_list.head
        x=tmp.endtime-tmp.starttime
        while(tmp):
            y=tmp.endtime-tmp.starttime
            if y>x:
                x=y
                a=tmp.id_no
            tmp=tmp.next
        return a, int(x)
    
    #Function responsible for searching the task having minimum execution time among all the tasks
    def get_minimised_timed_task(self):
        tmp=self.linked_list.head
        x=tmp.endtime-tmp.starttime
        while(tmp):
            y=tmp.endtime-tmp.starttime
            if y<x:
                x=y
                a=tmp.id_no
            tmp=tmp.next
        return a, int(x)
    
    #Function responsible for calculating average of the all execution times of the tasks in the linked list
    def get_average_time_of_all_tasks(self):
        sum=0
        countofLL=0
        tmp=self.linked_list.head
        while(tmp):
            x=tmp.endtime-tmp.starttime
            sum=sum+x
            countofLL=countofLL+1
            tmp=tmp.next
        average_time=sum/countofLL
        return int(average_time), sum, countofLL