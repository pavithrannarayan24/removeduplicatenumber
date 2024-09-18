#remove duplicate number in list
my_list1=[1,2,32,4,2,1,3,32,5,6,5,6,7,1]
#we using dict build function to remove duplicate number in a list
unique_list=list(dict.fromkeys(my_list1))
print(unique_list)