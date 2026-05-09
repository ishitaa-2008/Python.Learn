####setss########

#list
#dict

# unoerdered (no indexing)
#mutable (can add, but cannot change)
#unique elements(no duplicates)
#heterogeneous (can contain diff data type)



# b={}
# print(type(b))

# a=[]
# b={}
# s = set() #type coversion


# s= set()#empty set
# s={1,2,3,4,5}
# print(type(s))


#methods in sets
# 1)add()
# 2)update()
# 3)remove()
# 4)pop()
# 5)clear()
# 6)discard()

#1) add()  #for adding single element/value
# s = {1,2,3,3,4,5,}
# s.add(6)
# print(s)


#2)update() #for adding multiple elements
s = {1,2,3,3,4,5}
# s.update([7,8,9])

# print(s)

#duplicate values are not allowed in sets

#3)remove()
# s.remove(5)
# print(s) #if thevvalue is not present u will get an error


##4)discard()
# s.discard(10)

# 5)pop()
# print(s.pop()) #removes the smallest element frm the set


#5)clear()
# s.clear() #removes all the elements and return empty set
# print(s)

# """""""""""
# speacial methods
# union
# intersection
# difference
# symmetric difference
# """"""""""""

s1={1,2,3,4}
s2={2,3,4,6}
# print(f"Intersection:{s1.intersection(s2)}")
# print(f"union:{s1.union(s2)}")
# print(f"difference s1:{s1.difference(s2)}")
# print(f"difference s1:{s2.difference(s1)}")
# print(f"symmetric difference:{s1.symmetric_difference(s2)}")
#esa element jo s1 m ho aur s2 m na ho or s2 m ho s1 m na ho

#frozenset
# fs = {10,20,30,40}
# fs=frozenset(fs)
# # fs.add(60)
# # print(fs)
# fs.remove(40)
# print(fs)

#it will not change anything as the set is frozen