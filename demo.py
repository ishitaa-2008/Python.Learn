#3 types of naming
#snake casing
#camel casing
#pascal case

employeeOne = 1 #camel case
EmployeeOne = 2 #pascal case
employee_one = 3 #snake case 

#data types
#numbers - int,float,complex
#string - str
#3boolean

a = 34
#print(type(a))

b = 0.4
#print(type(b))

c = 5/3
#print(type(c))

a = 12j
#print(type(a)

#string
name =  "ishita"
#print(type(name))

#boolean
a = True
#print(type(a))

#input()

#input()
#print("helloww")

#age = input("what is your age - ")
#print("hellow")


#ask for a no.

#num = input("please provide a no.-")
#ans will be in string use type conv-


a = '12'
newA = int(a)

#print(type(a))
#rint(type(newA))

a = 12
a = int(a)
#print(type(a))

#num = int(input("pls tell ur no. :-"))
#print(num)  use float otherwise error


#if u have a string and inside that str u hv int thn u can use int()func
#and if u hv a string and inside the string u hv deciml or fraction u should use float() func

a = 12
a = float (a)
#print(a)

# if u hv a str and inside that str u hv int aswell as float use float()

bool()

a = 12
b = 0
c = ""
d = 0.0
f = "heloww"

#print(bool(a))
#print(bool(b))
#print(bool(c))
#print(bool(d))
#print(bool(f))

#falseyy - false
# 0, False, 0.0 , "", [] ,{} , ()

name = "ishita"
age = 18 

#print("your name is -" ,name,"and your age is ",age)

#bettr method

name = "ishita"
age = 18

#print(f"your name is {name} amd ur age is {age}")


#name = input("pls tell ur name:")
#age = int(input("what is ur age:"))
#print(f"your name is {name} amd ur age is {age}")



#operators
# arithematic opr - +,-,/,*,//,**,%
#comparison opr
#assignment opr
#logical opr 

#p = float(input("pls enter ur principle amt:"))
#r = float(input("pls enter rate of intrest:"))
#t = float(input("tell ur time in years:"))

#result = (p * r * t)/100
#print(f"ut si will be {result}")


#comp intrest

# p = float(input("pls enter ur principle amt:"))
# r = float(input("pls enter ur rate if int:"))
# t = float(input("enter time in years:"))

# ci = p * (1+ (r/100))**t
# print(f"ur comp int will be- {ci - p}")


#comparison operatorss -  (==, >,<, >= ,<= , !=)
# these operators will compare bw two things
#ans thwy will produce output in boolean

# print(12==12)
# print(12 > 12.1)

#LOGICAL OPR - (and , or , not)
#and - ekbi false hua to sare false hojaenge

# print(12 == 12, 56 == 56)
# print(12 == 12 and 56 == 56 and 34>23)
#all three opewration must be true if a single operation is false the final result is also going to be false

#or
# print(12>34 or 13 == 45 or 56 == 78 or 12==12)
# if any one of the operation is true the whole result will be true

#not
# print(not 12 == 12)
#it converts true to false and false to true


# print( not (12==12 and 34==34)and (13 ==56 or 34 !=45))
#print(bool(0) and 12 == 12)

#control flow
#(if else , loops , functions ,elif)

# age = int (input("enter your age :"))

# if age >= 18:  # true
#     print("u can vote")

# # if age <= 18:  #false
# #     print("u cannot vote")
# #bettr option
# else:  # else k aage kuch nahi likh skte
#     print('u cannot vote')




# a)10 b)20  c)30 d)40

# ans = input("pls select ur opt-")

# if ans == "a":
#     print("10 is the wrobg and")
# elif ans == "b":
#     print("20 is wrong ans")
# elif ans == "c":
#     print("30 is wrong")
# else:
#     print("40 is the correct ans")



#ques

# a = int(input("enter your first no.-"))
# b = int(input("enter your second no.-"))
# if a>b:
#     print("a iS greatest")
# elif b>a:
#     print("b is greatest") #agr dono same h to automatically else chl jaega kyuki 1st wrong hoga thus use elif
# else:
#     print("both r equal")    



# gen = input("pls tell your gender as char (M or F)")
# if gen == "M" or gen== "m":
#     print("good morning sir")
# elif gen == "F" or gen == "f":
#     print("good morning mam")
# else:
#     print("unknown gender")

# a = int(input("enter your no.-"))
# if a%2 == 0:
#     print("no. is even")
# else:
#     print("no. is odd")



# name = input("enter your name-")
# age = int(input("enter your age-"))
# if age>18:
#     print(f"heyy {name} you are eligible to vote")
# else:
#     print(f"heyy {name} u are not a valid voter u can vote after {18 - age} years")



# a = int(input("enter your no.-"))
# if 10 <= a <= 50:  #if a>= 10 and a<= 50
#      print("no is in range")
# else:
#      print("no. is out of range")


# engmarks = int(input("enter your marks in eng -"))
# mathsmarks = int(input("enter your marks in maths -"))
# if engmarks>=40 and mathsmarks>= 40:
#     print("you passed")
# elif mathsmarks >= 80 or engmarks >= 80:
#     print("you passed")
# else:
#     print("you failed")

#if (engmarks>=40 and mathsmarks>= 40) or (mathsmarks >= 80 or engmarks >= 80):

#bettr opt


# ch = input("enter your character :")
# if ch== "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#     print("its a vowel")
# else:
#     print("consonant")

# if ch in "AEIOUaeiou": #bettr opt



# year = int(input("pls enter year:"))
# if year % 100 == 0 and year % 400 == 0:
#      print("your is a leap year") 
# elif year % 100 != 0 and year % 4 == 0:
#      print("your is a leap year")
# else:
#      print("normal year")



# a = int(input("enter your no.-"))
# if a%3 == 0 and a%5 == 0: #or (a%7 == 0 and a%10 != 0)
#     print("no. is a special no.")
# elif a%7 == 0 and a%10 != 0:
#     print("no. is a special no.")
# else:
#     print("not a special no.")

#string

# a = "hello"
# print(a[4],a[-1])

#string slicing

# a = "SHERIYANS"
# # print(a[0:4:3])
# #[default value(0):last word:1[default value}]

# s = "hello how are you"
# print(s[14:])

# print(ord("A"))

# a=input("enter a char")
# value=ord(a)
# if (value>=65 and value<=90) or (value>=97 and value<=122):
#     print("is a char")
# else:
#     print(" a special char")

#loops
# a = (range(1,10,1))

# for i in a:
# #     print(a)for i in range

# #or
# (1,11,2):
#     print(i)

# for i in range(50,151,1):
#     print(i)

# for i in range(20,31,1):
#     print(i)

# for i in range(-12,11,1):
#     print(i)

# for i in range(10,-11,-1):
#     print(i)


# for i in range(5,51,5):
#     print(i)

# a = int(input("enter a no."))
# for i in range(a,a*10+1,a):
#     print(i)


# for i in range(100):
#     print("helloww world")


# n = int(input("enter stop point-"))
# for i in range(1,n+1,1):
#      print(i)

# n = int(input("enter a no."))
# for i in range(n,0,-1):
#     print(i)

# n = int(input("enter a no."))
# for i in range(1,11,1):
#      print(f"{n} x {i} = {n*i}")

#a=0
#a=a+1
#a=a+i

# n = int(input())
# sum = 0
# for i in range(1 , n+1):
#      sum += i
# print(f"sum = {sum}")

#sir
# n = int(input())
# a = 0
# for i in range(1 , n+1):
#      a = a + i
# print(f"sum = {a}")

#dry run
#a=0+1
#a=1+2
#a=3+3

# n = int(input("enter a no.-"))
# fact = 1
# for i in range(1 , n+1):
#     fact = fact * i
# print(f"factorial= {fact}")



# n = int(input("enter a no.-"))
# evensum = 0
# oddsum=0
# for i in range(1 , n+1 , 1):
#      if i%2==0:
#          evensum = evensum + i
#      else:
#          oddsum = oddsum + i
# print(f"even sum is{evensum} and oddsum is {oddsum}")


# n = int(input("enter a no.-"))
# for i in range(1,n+1,1):
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

# n = int(input("enter a no. whose factors u want -"))
# for i in range(1,n+1,1):
#     if n%i==0:
#         print(i)

#special no.
# n = int(input("enter a no. whose factors u want -"))
# sum = 0
# for i in range(1,n,1):
#      if n%i==0:
#          sum=sum+i
# if sum ==n:
#      print("no. is perfect")
# else:
#      print("not perfect")


#prime no.
# n = int(input("enter a no. -"))
# count = 0
#for i in range(1,n+1,1): 
#      if n%i==0:
#           count = count + 1
# if count == 2:
#      print("prime no.")
# else:
#      print("composite no.")

#or
# n = int(input("enter a no.-"))
# for i in range(2,(n//2)+1):
#     if n%i==0:
#        print("your no. is not prime")
#        break
# else:
#     print("your no. is prime")    


# n = int(input("enter a no.-"))
# for i in range (2,n//2+1):
#     if n%i == 0:
#         print("ur no. is composite")
#         break
# else:
#     print("ur no. is prime")



#while loop
# a = 10
# while a>0:
#     print(a)
#     a=a-1



# a=2345566
# while a > 0:
#     print(a%10)
#     a = a//10


# n = int(input("enter a no.: "))
# for num in range(2, n+1):
#     for i in range(2, num//2 + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num)


# n = int(input("enter a no.: "))
# sum=0
# while n!=0:
#     sum = sum + n%10
#     n=n//10
# print(sum)


# n = int(input("enter a no.: "))
# a=n
# rev = 0
# while n>0:
#     rev = rev *10 + n%10
#     n=n//10
# if(rev==a):
#     print("palindrome")
# else:
#     print("not a palindrome")



# n = int(input("enter a no.: "))
# a=0
# while n >0:
#     a = a*10 + n%10
#     n=n//10
# print(a)


#stringss in reverse,lenghth,in uppercase, lowercase, and copy into another string

# s = "shery"
# print(f"reverse of a string-{(s[::-1])}")

# print(f"length of string - {len(s)}")

# print(f"string in uppercase - {s.upper()}")

# print(f"string in lowercase - {s.lower()}")


#arrange strings character such that lowercase characters should come first
# s = "ShEry"
# lower = ""
# upper = ""
# for i in s:
#     if i.islower():
#         lower = lower + i
#     elif i.isupper():
#         upper = upper + i
# print(lower + upper)
         

#2 sheet
# str1 = "@#$$^ASD567Fghghkjh"
# alpha = 0
# digit = 0
# special = 0
# for i in str1:
#     if i.isalpha():
#         alpha = alpha + 1
#     elif i.isdigit():
#         digit = digit + 1
#     else:
#         special = special + 1
    
# print(f"alphabet count: {alpha}")
# print(f"digit count: {digit}")
# print(f"special count: {special}")


#34 compare two strings without using inbuilt func.

# str1 ="hello"
# str2 ="hello"
# if len(str1) == len(str2):
#     for i in range(len(str1)):
#         if  str1[i] != str2[i]:
#              print("strings r not same")
#              break
#     else:
#             print("strings r same")
# else:
#     print("both strings r not of same lenghth")



# a = input("enter a string-")
# vowels = 0
# for i in a:
#     if i in "AEIOUaeiou":
#         vowels = vowels + 1
# print(f"total count of vowels are :{vowels}") 


# ch = input("enter your character :")
# if ch== "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#     print("its a vowel")
# else:
#     print("consonant")

# if ch in "AEIOUaeiou": #bettr opt



# check palindrome
# n = (input("Enter a string: "))
# if str(n)==str(n)[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


# def countvowels():
#     a = "ishita"
#     vowels = 0
#     for i in a:
#         if i in "AEIOUaeiou":
#             vowels = vowels + 1
#     return f"total count of vowels are :{vowels}"

# print(countvowels())



# str = "hello"
# rev = ""
# for i in str[::-1]:
#     rev = rev + i
# print(rev)

#count vowels and consonents frm a string
# str = "ishita"
# vowels = 0
# consonant = 0
# for i in str:
#     if i in "aeiouAEIOU":
#         vowels = vowels + 1
#     else:
#         consonant = consonant + 1
# print(f"total vowels are {vowels} and total consonant are {consonant}")



# str = "hello"
# for i in str[::-1]:
#     print(i)


#palindrome
# def pallindrome():
#     a= "madam"
#     rev=a[::-1]
#     if rev == a:
#         print("string is pallindrome")
#     else:
#         print("no a pallindrome")
# pallindrome()


#to count the digits of a no.
# n = 1234
# count = 0
# while n>0:
#     digit = n%10
#     count = count + 1
#     n = n//10
# print(count)



# def count(n):
#     count = 0
#     while n>0:
#         digit = n%10
#         count = count + 1
#         n = n//10
#     print(f"count is {count}")
# count(123)



#if we use return inside a func. it will act like a mini variable until we didnt print a variable
#output will not be displayed



# def sum(n):
#     sum=0
#     while n!=0:
#         sum = sum + n%10
#         n=n//10
#     return f"sum is {sum}"
# print(sum(123))

# n = int(input("enter a no.: "))
# sum=0
# while n!=0:
#     sum = sum + n%10
#     n=n//10
# print(sum)
    
# def sum(n):
#     sum=0
#     while n!=0:
#         sum = sum + n%10
#         n=n//10
#     print(f"sum is{sum}")
# sum(123)

          
# def count(n):
#     count = 0
#     while n>0:
#         digit = n%10
#         count = count + 1
#         n = n//10
#     return f"count is {count}"
# print(count(123))






    












        






































    









