# # a=int(input("Enter the starting number"))
# # b=int(input("Enter the ending number"))
# # sum=0
# # while (a<=b and ):
# #     sum=sum+a
# #     if(a<b):
# #         print(a,end='+')
# #     else:
# #         print(a,"=",sum)
# #     a=a+1
# a=int(input("Enter the starting point = "))
# b=int(input("Enter the ending point = "))
# c=int(input("Enter the number of even digit sum you want = "))
# temp= 0
# sum = 0
# while(a<=b and a%b==0):
#     sum=sum+a
#     if(a<b-1):
#         print(a,end='+')
#     elif(a<=b ):
#         print(a,"=",sum)

        
a=int(input("Enter the number you want to print"))
sum=0
for i in range(1,a+1):
    sum=sum+i*2
    if(i<a):
        print(i*2,end='+')

    else:
        print(i*2,"=",sum)