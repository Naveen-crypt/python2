# mytext="Hello moto python is here"
# print("hello" in mytext)
# print("Hel"in mytext)
# print("moto" in mytext)
# print("is here" in mytext)

# **********************
# mylist=["Bob","Oggy","Olly"]
# print("Bob" in mylist)
# print("bob" in mylist)
# print(id(mylist))
# **************************************

# a=10
# # b=20
# b=10
# print(a is b)
# print(id(a))
# print(id(b))
# *****************************************

# age=eval(input("Enter your age = "))
# if(age<18):
#     print("You are not eligible for vote")
# else:
#     print("your are eligible for voting")

# *********************************************************
# a="hello"
# b="python"
# c=eval('a+b')
# print(eval('a+b'))
# print(type(c))
# **************************************

# check=eval(input(("Enter your expression = ")))
# print(check)
# *************************************

# CONVERSIONS
# a=15
# hexa=0x11
# print("Binary = ",bin(a))
# print("Octal = ",oct(a))
# print("Hexa-decimal = ",hex(a))
# print("Binary = ",hexa)
# ********************************

#POWER/EXPONENT
# a=2
# print(2e2)
# print(2*10**2)
# x=2e2
# y=2*10**2
# print(type(a),type(x),type(y))
# ******************************************

# COMPLEX NUMBERS
# a=5+3j
# b=1+2j
# print(type(a))
# print(a+b,"\n",a-b)
# print(a*b)
# a=True
# b=False
# print(a)
# print(b)
# print(a+a)
# print(a+b)
# print(b+b)
# c=a+a+a+a
# d=b+a
# e=bool(d)
# f=bool(c)
# print(c)
# print(d)
# print(type(c))
# print(type(d))
# print(e)
# print(f)
#********************************************************






# a=None
# print(type(a))
# b=1
# print(type(b))
# c="Naveen"
# print(type(c))
# *******************************************************

#Data types
# a=[34,6,4,7,44,76]
# b=bytes(a)
# print(type(a))
# print(type(b))
# print(b[2])
# byy=b'moto'
# print(byy[3])
 
# a="Naveen"
# print(a[2])
# val=ord(a[2])
# # print(val)
# # print(chr(118))
# print(ord(a[2]))

#**************************************************


# mylist=[2,3,5,6,8,6,5,3]
# print(mylist)
# mylist[0]=100
# print(mylist)


#****************************************
#            HIGHER-ORDER FUNCTIONS
# MAP

# ml=[1,2,3,4,5]
# def sqr(n):
#     return n**n
# result=map(sqr,ml)
# print(result)
# print(list(result))
#***********************

#  FILTER
# mylist=[]
# def even(n):
#     if(n%2==0):
#         return n
#     else:
#         pass

# for i in range(0,20):
#     mylist.append(i)
# result=filter(even,mylist)
# print(list(result))


# mylist=[]
# def odd(n):
#     if(n%2==0):
#         return n
# for i in range(0,100):
#     mylist.append(i)
# result=filter(odd,mylist)
# print(list(result))
# ********************************************************


#REDUCE
# import functools
# mylist=[1,2,3,4,5]
# def smm(a,b):
#     result=a+b
#     return result
# result=functools.reduce(smm,mylist)
# print("Sum = ",result)
# **********************************




# import functools
# mylist=[45,44444,25,76,34,87,23,8,5,1,4,7,88,5,333,6,8,88,44,7,33,578,2,2,2345,789,]
# def maxx(a,b):
#     if(a>b):
#         return a
#     else:
#         return b
# maxy=functools.reduce(maxx,mylist)
# print("Your max value = ",maxy)
# ****************************************************************




# LAMBDA

# check=lambda:print("Testing complete for lambda.")
# check()

# a=lambda p,q,r:2*p+2*q+2*r
# print(a(1,2,3))

# mylist=[1,2,3,4,5,6]
# def sqr(n):
#     return n**2
# x=lambda ls:print(list(map(sqr,ls)))
# x(mylist)

# a=[1,2,3,4,5]
# b=[6,7,8,9,1]
# addition=list(map(lambda x,y:x+y,a,b))
# print(addition)

# words=["ram","ravan","hanuman"]
# uppercased=list(map(lambda s:s.upper(),words))
# print(uppercased)

# loly=lambda n: [x for x in range(1,n+1) if x%2==0]
# print(loly(20))

grade=lambda x:'A'if x>=90 else('B'if x>=80 else('C' if x>=70 else'F'))
print(grade(88))
print(grade(93))
print(grade(23))






































































