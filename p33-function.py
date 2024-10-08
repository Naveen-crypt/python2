# #FUCNTION :- IT IS A BLOCK OF CODE WHICH IS USED TO ACHIEVE CODE REUSABILITY

# def add(a,b):
#     sm=a+b
#     return(sm)
# a=int(input("Enter 1st number = "))
# b=int(input("Enter 2nd number = "))
# result=add(a,b)
# print("Your answer = ",result)


# a=eval(input("Enter your data = "))
# print(a)

# print("Data type = ",type(a))



# a=eval(input("Enter your data = "))
# def length(a):
#     flag=0
#     for i in a:
#         flag=flag+1
#     return(flag)
# length=length(a)
# print("Length of the your data = ",length)

# x=10

# if type(x)==int:
#     print("OKKKKKKK")
# else:
#     print("NOOOOOOO")
# def summ(a,b):
#     result=a+b
#     print("a= ",a)
#     print("b= ",b)
#     return result
#     print("Function executed successfully")
# a=int(input("Enter 1st value = "))
# b=int(input("Enter 2nd value  = "))
# r=summ(b=a,a=b)
# print("Your result of sum  = ",r)
#***************************************************************************************8



# a=eval(input("Enter your data"))
# if type(a) == str:
#     print("It's a string data")
# elif type(a) == int:
#     print("It's an interger data")
# else:
#     print("It's another type of data")
# *****************************************************************************************











def add(*a):
    print(a)
    print("data type = ",type(a))
    sm=0
    for i in a:
        for x in i:
            sm=sm+x
    return sm

a=eval(input("Enter your tuple data = "))
result=add(a)
print("Your result = ",result)












































