list1=["apple","orange","graps"]
list2=["pinaple","mango",342,65,21]

print(list1,list2)

list3=list2+list1
print(list3)


# remove 3rd index and insert the name

list3[3]="banana"
print(list3)


# in operator

print("orange" in list1)



# list functions

# appand()    add last index

list3.append("jack fruit")
print(list3)

# insert()    add perticular index

list3.insert(4,"watermelone")
print(list3)
print(len(list3))
print(list3.index("apple"))

