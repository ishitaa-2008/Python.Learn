#1
#reverse of a no. using for loopapproach by slicing
# n = input("Enter a number: ")
# print(n[::-1])

#2
#now by loop
# n = int(input("Enter a number: "))
# rev = " "
# for i in str(n)[::-1]:
#     rev+= i
# print(rev)


#3
#print hello world 5 times
# str= "hello world"
# for i in range(1,6):
#     print(str)

#4
#optimal way of printing hello world 5 times
# print("hello world\n" *5)

#5
#fibonacci series
# a=0
# b=1
# for i in range(5):
#     print(a)
#     a,b=b,a+b

#6
#find the largest digit from the no.
# n = int(input("Enter a number: "))
# large=0
# for i in str(n):
#     a=int(i)
#     if(a>large):
#         large=a
# print(large)    



#7
#guessing game
# import random
# i = random.randint(1,10)
# for x in range(5):
#   n= int(input("guess the no."))
#   if(i==n):
#    print("correct guess")
#    break
#   elif(n<i):
#    print("urno. is less than original no.")
#   elif(n>i):
#    print("ur no. is grater than the original")
# else:
#  print(f"{i} was the correct num")


#8
# check palindrome
# n = int(input("Enter a number: "))
# if(str(n)==str(n)[::-1]):
#     print("palindrome")
# else:
#     print("not palindrome")


#9
#keep taking inputs until user takes 0 , print the sum of inputs
# sum = 0
# while True:
#     i = int(input("Enter a number: "))
#     if(i==0):
#         break
#     else:
#         sum+=i
# print(sum)    


#10
# n=1234
# rev = 0
# while n != 0:
#      rev= rev*10 + n%10
#      n=n//10
# print(rev)

#11
# check armstrong or not
# n=153
# copy = n
# sum = 0
# length = len(str(n))
# while n>0:
#     digit = n%10
#     sum = sum + digit**length
#     n=n//10
# if(copy == sum ):
#     print("armstrong no.")
# else:
#     print("not an armstrong no.")








 