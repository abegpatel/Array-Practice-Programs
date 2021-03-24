# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:12:02 2021

@author: Abeg
"""

#all symmetric pair of an array
def symmetricpair(pairs):
  s=set()
  for (x,y) in pairs:
    s.add((x,y))
    if (y,x) in s:
      print((x,y),"|",((y,x)))
pairs=[(11,20),(30,40),(5,10),(40,30),(10,5)]
print(symmetricpair(pairs),end="")
#repeating element
n=int(input("enter the size"))
arr=[]
for i in range(0,n):
  e=int(input())
  arr.append(e)
x=list(dict.fromkeys(arr))
for i in x:
  if(arr.count(i)>1):
    print(i)
  
#non-repeating element
n=int(input("enter the size"))
arr=[]
for i in range(0,n):
  e=int(input())
  arr.append(e)
x=list(dict.fromkeys(arr))
for i in x:
  if(arr.count(i)==1):
    print(i)
#no of even element and odd elemnet in an array
arr=[]
n=int(input())
count1=0
count2=0
for i in range(n):
  e=int(input())
  arr.append(e)
for i in range(n):
  if(arr[i]%2==0):
    count1+=1
  else:
    count2+=1
print("no of even",count1)
print("no of odd is",count2)

#finding min scalarproduct of two vector
arr1=[]
arr2=[]
n=int(input("size of the  array"))
for i in range(n):
  e=int(input())
  arr1.append(e)
for i in range(n):
  e=int(input())
  arr2.append(e)
list=()
arr1.sort()
arr2.sort(reverse=True)
sum=0
for i in range(0,n):
  sum=sum+arr1[i]*arr2[i]
print(sum)
#minimum abs difference of given array
arr=[5,10,1,4,8,7]
n=len(arr)
sum=0
arr.sort()
sum=sum+abs(arr[0]-arr[1])
sum+=abs(arr[n-1]-arr[n-2])
for i in range(1,n-1):
  sum+=min(abs(arr[i]-arr[i-1]),abs(arr[i]-arr[i+1]))
print(sum)
#finding max scalarproduct of two vector
arr1=[]
arr2=[]
n=int(input("size of the  array"))
for i in range(n):
  e=int(input())
  arr1.append(e)
for i in range(n):
  e=int(input())
  arr2.append(e)
list=()
arr1.sort()
arr2.sort()
sum=0
for i in range(0,n):
  sum=sum+arr1[i]*arr2[i]
print(sum)
# Function to return maximum product of a sublist of given list
def maxProduct(A):
	max_ending = min_ending = 0
	max_so_far = 0
	for i in A:
		temp = max_ending
		max_ending = max(i, max(i * max_ending, i * min_ending))
		min_ending = min(i, min(i * temp, i * min_ending))
		max_so_far = max(max_so_far, max_ending)
	return max_so_far
if __name__ == '__main__':
	A = [6,-10,-3,0,5]
	print("The maximum product of a sublist is", maxProduct(A))

#check frequency of each char
n=int(input("enter the size"))
arr=[]
for i in range(0,n):
  e=int(input())
  arr.append(e)
x=list(dict.fromkeys(arr))
for i in x:
  print("{}occours {} time".format(i,arr.count(i)))
#removing duplicate element prom an array
n=int(input("enter the size"))
arr=[]
for i in range(0,n):
  e=int(input())
  arr.append(e)
x=list(dict.fromkeys(arr))
print(x)
#distinctelement
n=int(input("enter the size"))
arr=[]
for i in range(0,n):
  e=int(input())
  arr.append(e)
x=list(dict.fromkeys(arr))
print(x)
print(len(x))
#ARR is disjoint or not
def disjoint(arr1,arr2):
  for i in range(0,len(arr1)):
    for j in range(0,len(arr2)):
      if(arr1[i]==arr2[j]):
        return -1
      else:
        return 1
arr1=[1,2,3,4]
arr2=[1,2,3,4]
res=disjoint(arr1,arr2)
print(res)
if(res==-1):
  print("not disjoint")
else:
  print("disjoint")

#dtermine array is a subset of anthor array or not
def subset(arr1,arr2,m,n):
  i=0
  j=0
  for i in range(n):
    for j in range(m):
      if(arr2[i]==arr1[j]):
        break
    if(j==m):
      return 0
  return 1
arr1=[1,2,3,4]
arr2=[2,3]
m=len(arr1)
n=len(arr2)
if(subset(arr1,arr2,m,n)):
  print("arr2 is a subset of arr1")
else:
  print("not")
#rotation from left to right
arr=[10,20,30,40,50]
k=int(input("enter the no of rotation"))
k=k%len(arr)
for i in range(k):
  x=arr.pop(-1)
  arr.insert(0,x)
print(arr)
#all no array be made equal
def make_equal(arr,n):
  for i in range(n):
    while(arr[i]%2==0):
      arr[i]=arr[i]/2

    while(arr[i]%3==0):
      arr[i]=arr[i]/3

  for i in range(n):
    if arr[i]!=arr[0]:
      return False
    else:
      return True

arr=[3,50,75,100]
n=len(arr)
if(make_equal(arr,n)):
  print("yes")
else:
  print("no")
#sum of dight in the array
def sumarr(arr,n):
  for i in range(n):
    temp=arr[i]
    sum=0
    while(temp>0):
      d=temp%10
      sum=sum+d
      temp=temp//10
    print(sum,end=" ",sep=" ")
arr=[]
n=int(input("size"))
for i in range(n):
  e=int(input())
  arr.append(e)
sumarr(arr,n)

#placed all even no followed odd no
# variables
def rearrangeEvenAndOdd(arr, n) :
  j = -1
  for i in range(0, n) :
    if (arr[i] % 2 == 0) :
        j = j + 1

        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
n=int(input("fj"))
arr=[]
for i in range(n):
  arr.append(int(input()))
rearrangeEvenAndOdd(arr, n)
for i in range(n):
  print(arr[i],end=" ",sep=" ")
#array rotation
def leftrotate(arr,d,n):
  for i in range(d):
    leftrotateone(arr,n)
def leftrotateone(arr,n):
  temp=arr[0]
  for i in range(n-1):
    arr[i]=arr[i+1]
  arr[n-1]=temp
arr=[1,2,3,4,5,6]
print(arr)
leftrotate(arr,2,len(arr))
print(arr)
#max Element in an array
def largeelearray(arr):
  max=arr[0]
  for i in range(0,len(arr)):
    if arr[i]>max:
      max=arr[i]
    else:
      max=max
  return max
arr=[1,2,3,4]
print(largeelearray(arr))
#recurrent element in an array
def recurr(arr,n):
  for i in range(0,n):
    for j in range(0,n):
      if arr[i]==arr[j+1]:
        return arr[i]
      else:
        return False
arr=[2,5,1,2,3,5,1,2,4]
n=len(arr)
print(recurr(arr,n))
#O(n^2)
#o(1)
#sum of array
def sumarray(arr):
  sum=0
  for i in range(0,len(arr)):
    sum=sum+arr[i]
  return sum
arr=[1,2,3,4]
print(sumarray(arr))
#Twosum array
"""
def twosum(arr,target):
  outputarr=[]
  for i in range(0,len(arr),1):
    for j in range(i+1,len(arr),1):
      if (arr[j] == target - arr[i]):
          outputarr.append(i)
          outputarr.append(j)
          return outputarr
target=int(input("uju"))
arr=[2,3,4,5]
print(twosum(arr,target))"""
"""
def twosum(arr,target):
  outputarr=[]
  for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
      sum=arr[i]+arr[j]
      if sum==target:
        outputarr.append(i)
        outputarr.append(j)
        return outputarr
print(twosum(arr=[2,7,11,15],target=9))"""

