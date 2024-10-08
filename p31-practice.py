# # # # # a=int(input("Enter the starting range"))
# # # # # b=int(input("Enter the ending point"))
# # # # # odd=0
# # # # # even=0
# # # # # for i in range(a,b+1):
# # # # #     if(i%2==0):
# # # # #         even=even+1
# # # # #     else:
# # # # #         odd=odd+1
# # # # # print("odd = ",odd)
# # # # # print("even = ",even)
# # # # x =range(-4,5,2)
# # # # print(tuple(x))
    
# # # for i in range(1,11):
# # #     if i==4 or i==7:
# # #         continue
# # #     else:
# # #         if(i<10):
# # #             print(i,end=',')
# # #         else:
# # #             print(i)
# # for i in range(1,-100,-1):
# #     if(i==56 or i==57):
# #         break
# #     else:
# #         print(i,end=',')
# a=0
# for i in range(1,10):
#     a=a+1
#     print(a,end=',')
#     i=i-2
#     print(i)
    
while True:
    print("1.For addition\n2.For substraction\n3.For multiplication\n4.For division\n5.Exit")
    opt=int(input("Enter your option = "))
    if opt in (1,2,3,4):
        a=int(input("Enter first value = "))
        b=int(input("Enter second value = "))
        if(opt==1):
            print("Ans = ",a+b)
        elif(opt==2):
            print("Ans = ",a-b)
        elif(opt==3):
            print("Ans = ",a*b)
        else:
            print("Ans = ",a/b)
    elif(opt==5):
        break
    else:
        print("Please enter valid value for execution")