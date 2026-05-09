#user defined function
#to create a func. def func. name () keyword is use

# def greeting(): #defining a func.
#     print("hello good morning")

# greeting() #calling of a func.
# greeting()
# greeting()



#parameters and arguments

# def addition(a,b): #a and b are parameters
#     print(a+b)

# addition(10,20)


# def palindrome(n): #a and b are parameters
#   a=n
#   rev = 0
#   while n>0:
#      rev = rev *10 + n%10
#      n=n//10
#   if(rev==a):
#      print("palindrome")
#   else:
#      print("not a palindrome")


# palindrome(121)
# palindrome(346)


#types of arguments
#1 positional argu

# def multiply(a,b): #fixed position
#     print(a*b)

# multiply(6,7) #fixed positional argu


#2 default argument
# def info(name,age):
#      print(f"your name is  {name} and ur age is{age}")

# info (age = 12, name = "raj" )



# def nos(a,b,c,d,e):
#      print(a,b,c,d,e)


# nos(12,34,e=64, c=12, d= 67)
#if u give a value using default arguments u always hv to give further values using default argu


# def info(name,age,id = None):
#     print("info received")

# info("ishita", 18 ,8970)

#return
#def hello():
#     return "hello how r u"
#print(hello())



# def strongnumber(n):
#     sum=0
#     copy = n
#     while n>0:
#         z= n%10
#         fact = 1

#         for i in range(1,z+1):
#             fact = fact * i

#         sum = sum + fact
#         n=n//10
#     if sum == copy:
#          print("strong no.")
#     else:
#          print(" not strong no.")

# strongnumber(145)



# def agechecker(n):
#     if n>=18:
#         return True
#     else:
#         return False
    
# age = int(input("enter ur age:"))
# if agechecker(age):
#     print("u can vote")
# else:
#     print("u cannot vote")





# def hello1():
#     hello2()
#     print("hello 1")

# def hello2():
#     hello3()
#     print("hello 2")

# def hello3():
#     hello4()
#     print("hello 3")

# def hello4():
#     print("hello 4")

# hello1()




# def numbers(n):
#      if n == 101:
#          return "done"
#      print(n)
#      numbers(n+3)
# numbers(1)

#reverse
# def numbers(n):
#      if n == 101:
#          return "done"
#      numbers(n+1)
#      print(n)
# numbers(1)








