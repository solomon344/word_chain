import tkinter
from tkinter import *
import string

class Chain:
    def __init__(self,head,target):
        self.head = head
        self.target = target
    
    switch = string.ascii_lowercase
    words = ["cat","rat","rot","lot","dog","dot","lat","log","rog","rag","dat","cot","cag"]
    steps = []
    Notfound  = True
    chain = ""
    def get_target(self):
        if self.head and self.target in self.words:
            self.steps.append(self.head)
            for i in range(len(self.target)):
                chain = self.head.replace(self.head[i],self.target[i])
                if chain in self.words:
                    self.steps.append(chain)
                    self.head = chain
                    if chain == self.target:
                        
                        break
                    continue
                else:
                    continue
        
            return " -> ".join(self.steps) + f"({len(self.steps) - 1} steps)"
        else:
            return "starting or target word not found"
        
        

        
                
            
head = input("enter startin word: ")
target = input("enter target word: ")

chain = Chain(head,target)
print(chain.get_target())