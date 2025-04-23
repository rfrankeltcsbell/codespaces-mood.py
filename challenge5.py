list1=[1,2,3]
list2=[4,5,6]

my_dict= dict(zip(list1,list2))

print(my_dict)

dict2= {}
for i in range(len(list1)):
    dict2[list1[i]]= list2[i]
print (dict2)
