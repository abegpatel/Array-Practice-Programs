# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:03:24 2021

@author: Abeg
"""

#array basic question
#array implementation
class myarray:
  def __init__(self):
    self.length=0
    self.data={}

  def get(self,index):
    return self.data[index]

  def push(self,item):
    self.data[self.length]=item
    self.length+=1
    return self.length

  def pop(self):
    lastitem=self.data[self.length-1]
    del self.data[self.length-1]
    self.length-=1
    return self.data

  def remove(self,index):
    item=self.data[index]
    self.shiftitems(index)
    
  def shiftitems(self,index):
    for i in range(0,self.length-1):
      self.data[i]=self.data[i+1]
    print(self.data[self.length-1])
    del self.data[self.length-1]
    self.length-=1
    print(self.data)

obj=myarray()
print(obj.push('hi'))
print(obj.push('hello'))
print(obj.push('!'))
print(obj.push('zero'))
print(obj.push('hati'))
print(obj.pop())
#print(obj.pop())
#print(obj.remove(1))
print(obj)

