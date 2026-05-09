#########file handling########

#modess
#w- write mode(agr file created ni h to hojaegi,agr purana data h to overwite hojaega)
#a- append mode(adds to the end of the file)
#r- read mode(read,file must exist(default mode,also creates))
#x- create mode(agr file already exist krti h to error aaega,)


# file = open('dictionary.py')
# print(file.read())
# file.close


# file = open('gangadhar.txt','w')
# file.write('this is a new file')
# file.close()

# file = open('gangadhar.txt','a')
# file.write('this is a new file with new added data in it')
# file.close()

# file = open('gangadhar.txt','r')
# for i in file:
#     print(i)
# file.close()


# file = open(r"C:\Users\ishit\OneDrive\Desktop\New Text Document.txt",'w')
# file.write('this is a new file')
# file.close()


#with statement(no need to close)
# with open('gangadhar.txt','r') as file:
#     print(file.read())
# with open('gangadhar.txt','w') as file:
#     file.write("content overwritten")
#     print("done")


#paths
# C:\Users\ishit\ccpython\gangadhar.txt
# from pathlib import Path
# p=Path("gangadhar.txt")
# if p.exists():
#     print("file exists")
# else:
#     print("doesnt exist")