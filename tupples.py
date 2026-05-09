#########tupples######
#properties of tuple
#1 tuple are ordered = indexing kr skte h
#2 tuple can hv dupicacy
#3 tuple are heterogeneous
#4 tuples are immutable
#5 tuples cant be updated

#t = () #empty tuple
#t= (1,2,3,4)
#for i in t :
#     print(i)


# t=(1,2,3,4,5)
# for i in range(len(t)):
#     print(i)



# t=(1,2,3,4,5)
# for i in t:
#     print(i) #direct loop

# for i in range(len(t)):
#     print(i,t[i]) #index loop

# for index, value in enumerate(t):
#     print(index,value) 

# print(t[2])

# print(t[1:4])




# """"""""
# methodss in tupples
# 1)count() we can count occurence of a value
# 2)index()



# t=(1,2,3,4,5,5,5,6,6,6,6)
# print(t.count(6))

# print(t.index(6)) #first occurence of 6


#membership operators
# print(3 in t)
# print(8 in t)


#tuple unpacking
# t=(1,2,3,4,5,6)
# # a,b,c,d,e,f = t
# # print(a)
# # print(b)
# # print(c)
# # print(d)
# # print(e)
# # print(f)


# #tuple packing
# a,b=(1,2)
# print(a)



#star expression(*)
# t=(1,2,3,4,5,6)
# a,*b ,c = t
# print(a)
# print(b) #middle value extraction
#print(c)


# t=(1,2,3,4,5)
# a,*b,c = t
# print(a)
# print(c)


#to merge two tupples
# t1=(1,2,4)
# t2=(5,7)
# print(t1+t2)

