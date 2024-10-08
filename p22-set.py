# my_set={54,45,23,'erggg','rggfgs',4546,'gergfg',4544,'gffd',54,54,'rtreyr','trytrhtrh',5656,45346,47,74,546,3434,4,'eyfhhrthg'}
# print(my_set)
# print("address",id(my_set))
# print("Type",type(my_set))
# print("Length of set = ",len(my_set))
a={1,2,3,4,5,6,7}
b={0,9,8,7,6,5,4,3}
print("Union of sets",a.union(b))
print("Intersection of sets = ",a.intersection(b))
print("Difference of sets = ",a.difference(b))
print("Differencce = ",b.difference(a))
print("Symmetric of sets = ",a.symmetric_difference(b))