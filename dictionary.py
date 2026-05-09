# dic = {"one": 1, "two": 2}
# print(dic["one"])

#create, mutable(only values can be changed )
# d={1:10,2:20}
# d[4]=40
# print(d)


#update
# d={1:10,2:20}
# d[1]=40
# print(d)

#delete
# d={1:10,2:20,3:30}
# del d[2]
# print(d)


#join both dictionary
# d1={1:10,2:20,3:30}
# d2={4:40,5:50,6:60}
# for j in d2:
#     d1[j]=d2[j]
# print(d1)

# d1={1:10,2:20,3:30}
# d2={4:40,5:50,6:60}
# for j in d2:
#     if j in d1.keys():
#         d1[j]=d1[j]+d2[j]
#     else:
#         d1[j]=d2[j]
# print(d1)


#countfreq
# l = [1,1,1,3,3,4,8,8,8,8]
# d={}
# for i in l:
#     if i in d.keys():
#         d[i] = d[i]+1
#     else:
#         d[i]= 1
# print(f"freq of elemants are {d}")


# a= {1:10,2:20,3:30}
# b= {3:40,5:50,6:60}

# for i in b:
#     if i in a.keys():
#         a[i]= a[i]+b[i]
#     else:
#         a[i] = b[i]


# print(a)



# l=[3,2,3,2,2,2]
# d={}
# for i in l:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# for i in d.values():
#     if i % 2 == 0:
#         print("pair")
#     else:
#         print("not pair")