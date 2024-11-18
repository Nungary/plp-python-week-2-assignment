#creating empty list 
my_list = []

#add items to list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert value 15 at the second position
my_list.insert(1, 15)

#extend my list 
my_list.extend([50,60,70])

#remove last element
del my_list[6]

#sort list in ascending order
my_list.sort()

#find and print index of value 30 in my list 
index_value_30 = my_list.index(30)
print("index of 30:", index_value_30)