# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:56:59 2021

@author: SamsunG i5
"""



from heapq import heappush, heappop, heapify  

class priorityqueue(object): 
    #initializes the queue with an empty list
    def __init__(self): 
        self.q = []   
    
    #Returns value of the queue
    def Print(self): 
        return self.q
    
    #checks if the queuee is empty or not
    def checkIfEmpty(self): 
        return len(self.q) == 0
    
    #Inserts a new node
    def insertNode(self, data): 
        self.q.append(data) 
    
    #deletes a node
    def del_Min(self): 
        try: 
            min = 0
            for i in range(len(self.q)): 
                if self.q[i] < self.q[min]: 
                    min = i 
            item = self.q[min] 
            del self.q[min] 
            return item 
        except IndexError: 
            print() 
            
class binaryheap: 
    
    #initializes the binary heap with an empty array
    def __init__(self): 
        self.heap = []    
    
    #Performs the Union
    def Union(self): 
        return heappop(self.heap) 
    
    #insert a new node
    def Insert(self, k): 
        heappush(self.heap, k)  
    
    #get the minimum value 
    def Min(self): 
        return self.heap[0]
    
    #deletes a node 
    def Del(self, i): 
        self.Update(i, float("-inf")) 
        self.Union()
        
    #updates the heap        
    def Update(self, i, new_val): 
        self.heap[i]  = new_val  
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]): 
            self.heap[i] , self.heap[self.parent(i)] = ( 
            self.heap[self.parent(i)], self.heap[i])  
    
    #get parent element
    def parent(self, i): 
        return (i-1)/2
    
    def PrintHeap(self):
        return self.heap
    
obj=binaryheap()
obj.Insert(1)
obj.Insert(2)
obj.Insert(9)
print(obj.PrintHeap())
obj.Del(0)
print(obj.PrintHeap())
obj.Update(0,15)
print(obj.PrintHeap())