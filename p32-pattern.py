# # # # # a=int(input("Enter your number of lines you want to print for the pattern = "))
# # # # # for i in range(0,a):
# # # # #     print("*"*i)
# # # a=int(input("Enter the number of lines = "))
# # # for i in range(1,a+1):
# # #     print((a-i)*" " + "* "*i)
# # # #*****************************************

# # # # a=int(input("Enter the number of line for the patter = "))
# # # # for i in range(1,a+1):
# # # #     print(())
# # a=int(input("Enter the number of line for the pattern = "))
# # for i in range(1,a+1):
# #     print((a-i)*" "+"* "*i)
# # for i in range(1,a):
# #     print(i*" "+(a-i)*"* ")
# #*********************************************************************************************


# a=int(input("Enter the number of lines = "))
# for i in range(1,a+1):
#     if(i==1 or i==a):
#         print("*"*a)
#     else:
#         print(("*"+" "*(a-2))+"*")
a=input("Enter your string = ")
def length(a):
    flag=0
    for i in a:
        flag=flag+1
    print("Your length  = ",flag)
length()