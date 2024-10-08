# # i=int(input("Enter the starting point"))
# # j=int(input("Enter the end point"))
# # while(i>=1 and j<=10):
# #     print(i,end=',')
# #     j=j+1
# # i=1
# # while i<=10:
# #     if(i==10):
# #         print(i)
# #         break
# #     print(i,end=(','))
# #     i=i+1
# ##***************************************************************
# a=int(input("Enter the starting point"))
# b=int(input("Enter the end point"))
# while a<=b:
#     if(a==b):
#         print(a)
#         break
#     print(a,end=',')
#     a=a+1
i=int(input("Enter the starting point"))
j=int(input("Enter the ending point"))
while(i<=j):
    if(i<j):
        print(i,end=',')
    else:
        print(i)
    i=i+1