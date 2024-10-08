a=int(input("Enter the starting point = "))
b=int(input("Enter the ending point = "))
aa=a
bb=b
#for printing odd number
while (a<=b):
    if(a%2==1):
        if(a<b-1):
            print(a,end=',')
        else:
            print(a)
    a=a+1
#for printing evend number
a=aa
b=bb
while (a<=b):
    if(a%2==0):
        if(a<b-1):
            print(a,end=',')
        else:
            print(a)
    a=a+1
#for printing prime numbers
a=aa
b=bb
for i in range (a,b+1):
    if(i>1):
        for i in range(2,i):
            if(a%i==0):
                break
        else:
            print(a,end=',')
    a=a+1