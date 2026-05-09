#data stuc - list, tupple, dictionary, set
#List

# a=12
# b=45
# c=67
# d=23
# e=45
#for creating a list u have to use square brakets []

# l = [12,45,67,23,45]

#special powers
#1 - heterogeneous nature - it can store any types of data types at once

# l= [12,"hello",12.67,True, print()] 

#2 - ordered - every element in list have a deignated position

#3 - mutable nature - (tupples r immutable)  - u can change anything inside the list at any point of time

#4 - duplicates - u can store duplicate elements inside list (set m ni hota duplicate)

#reading list
# a = [10,20,30,40,50]

#u will use indexing
# print(a)
# print(a[0],a[-1])


#updating a list
# a = [10,20,30,40,70]
# a[-1]=50
# print(a)

#delete
# a = [10,20,30,40,70]
# del a[-1]
# print(a)

# del a
# print(a)

#creating loops on list
# a = [10,20,30,40,50]

#based on values 

# for i in a:
#     print(i)

#here u will access all the values 10,20,30.....

#based on index
# for i in range(0,5):
#     print(i)


#this loop can access ur index aswell
#it gives more control over ur list
#agr index se values bi access krni ho
# for i in range(0,5):
#     print(a[i])


# for i in range(0,len(a)):
#      print(a[i])


#methods
#to add smth at the end
# a = [1,2,3,4]
# a. append(5)
# print(a)
 
# l = []
# for i in range(10,51,10):
#     l.append(i)

# print(l)

#insert
# a = [10,20,40,50]
# a.insert(2,30)
# print(a)

# a = [10,20,30]
# a.clear()
# print(a)

# saved = a.pop(1) # koi value ni di to last value delete hojaegi #based on index
# print(a)

# a.remove(10) #based on values
# print(a)

# a = [10,20,40,50]
# print(a.index(50))

# a.sort()
# print(a)


#quesssss

# a = int(input("how many elements u want"))
# l=[]
# for i in range(a):
#     z= int(input("tell ur nos."))
#     l.append(z)

# print(l)

# a = eval(input("how many elements u want"))
# print(a)


# a=[1,2,3,4,5,6]
# l=[]
# for i in range(len(a)-1,-1,-1):
#     l.append(a[i])
# print(l)

#dif method with pointer
# a=[1,2,3,4,5,6]
# z= len(a)-1

# for i in range(len(a)//2):
#     a[i],a[z] = a[z],a[i]
#     z = z-1

# print(a)



# a = [1,3,-9,7,-66,4]
# for i in a:
#     if i>=0:
#         print(i)
# for i in a:
#     if i <=0:
#         print(i)


###########sorting########## 


#bubble sort
# a=[56,12,89,23,56,90,13]

# for j in range(len(a)-1):
#     for i in range(0,len(a)-1-j):
#         if a[i]>a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]
# print(a)



# a=[56,12,89,23,56,90,13]
# largest=a[0]
# index=0
# for i in range(1,len(a)):
#     if a[i]> largest:
#         largest = a[i]
#         index=i

# print(f"largest element is {largest} at index {index}")

# 2nd largst element
# a=[6,12,23,56,90,13,89]
# largest=a[0]
# largestind=0
# seclargest=a[0]
# seclargestind=0

# for i in range(1,len(a)):
#     if  a[i] >largest:
#         seclargest=largest
#         largest=a[i]
#         seclargestind = largestind
#         largestind = i
#     elif a[i] >seclargest:
#         seclargest=a[i]
#         seclargestind = i

# print(largest , largestind)
# print(seclargest ,seclargestind)




# a=[56,12,23,56,90,13,89]
# smallest=a[0]
# smallestind=0
# secsmallest=a[0]
# secsmallestind=0

# for i in range(1,len(a)):
#     if  a[i] < smallest:
#         secsmallest=smallest
#         smallest=a[i]
#         secsmallestind = smallestind
#         smallestind = i
#     elif a[i] <secsmallest:
#         secsmallest=a[i]
#         secsmallestind = i

# print(secsmallest,secsmallestind)
# print(smallest,smallestind)





#check if the list is sorted or not
# l=[3,7,65,8,3]
# for i in range(len(l)-1):
#     if l[i]> l[i+1]:
#         print("list is not sorted")
#         break
# else:
#     print("not sorted")


#palindrome
# l=[2,3,15,15,3,2]
# for i in range(len(l)//2):
#     if l[i] != l[len(l)-1-i]:
#         print(" not apalindrome")
#         break
# else:
#     print("palindrome")


# a = int(input("how many elements u want"))
# l=[]
# sum=0
# for i in range(a):
#     z= int(input(f"tell ur nos. at index {i}:"))
#     sum += z
#     l.append(z)
# print(l)
# print(sum)



#or using map
# lst=list(map(int,input("enter elements").split()))
# print(lst)
#map(datatype,input)
#split(separates all the values an digits)
#list(convert the value in the form of list datas trucyture)
#sbse phle input accept,hr input split hoga,inputs will be typescasted in the form of int,
#we store all the int values inside a list



#rotate a list by k elements
# l=[1,2,3,4,5] #o//p = k=2,[4,5,1,2,3]
# k=2
# for i in range (k): #i-> 0,1
#     last = l[-1] #last value 5
#     for j in range(len(l)-1,0,-1):
#         l[j]=l[j-1]
#     l[0]=last
# print(l)



#assign all the 0s at the end of the list
# l=[0,1,0,3,12]
# j=0
# for i in range(len(l)):
#     if l[i] != 0:
#         l[i],l[j] = l[j],l[i]
#         j=j+1
# print(l)






