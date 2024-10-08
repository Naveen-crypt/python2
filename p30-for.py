# # # # # a=int(input("Enter the starting point = "))
# # # # # b=int(input("Enter the ending point = "))
# # # # # cont=[]
# # # # # for i in range(a,b+1):
# # # # #     if(i<b):
# # # # #         print(i,end=',')
# # # # #     else:
# # # # #         print(i)
# # # # #     cont.append(i)

    
# # # # # for i in range(a,b+1):
# # # # #     if(i%2==0):
# # # # #         if(i<b-1):
# # # # #             print(i,end=',')
# # # # #         else:
# # # # #             print(i)

# # # # # for i in range(a,b+1):
# # # # #     if(i%2!=0):
# # # # #         if(i<b-1):
# # # # #             print(i,end=',')
# # # # #         else:
# # # # #             print(i)

# # # # # print("list of continous = ",cont)
# # # # ##****************************************************************

# # # # for i in range(10,101,10):
# # # #     print(i)
# # # data=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
# # # even=0
# # # odd=0
# # # for i in data:
# # #     if(i%2==0):
# # #         even=even+1
# # #     else:
# # #         odd=odd+1
# # # print("Total even no. = ",even)
# # # print("Total odd no. = ",odd)
# # a=input("Enter your string = ")
# # vovel=0
# # cons=0
# # for i in a:
# #     if i in ['a','e','i','o','u']:
# #         vovel=vovel+1
# #     else:
# #         cons=cons+1
# # print("Vovels = ",vovel)
# # print("Cons = ",cons)
# a=input("Enter your string = ")
# vovel=0
# con=0
# for i in a:
#     if i in ['a','e','i','o','u','A','E','I','O','U']:
#         vovel=vovel+1
#     else:
#         con=con+1
# print("Total vovels = ",vovel)
# print("Total consonets = ",con)
# print("Total alphabets = ",vovel+con)
a=input("Enter your string = ")
small=0
capital=0
num=0
special=0
for i in a:
    if ord(i) in range(65,98):
         capital=capital+1
        
    elif ord(i) in range(97,123):
        small=small+1
       
    elif ord(i) in range(48,57):
        num=num+1
    else:
        special=special+1
print("Small letters = ",small)
print("Capital letters = ",capital)
print("Numbers = ",num)
print("Special Characters = ",special)
