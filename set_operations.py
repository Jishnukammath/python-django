
set1={1,"b",4,7,5,2,"c","r",3}
#or
# set1=set((1,2,3,4,5,6,3,4,5,2))

print(set1)
# for i in set1:
#     print(i)

print("r" in set1)

#adding

set1.add("v")
print(set1)

#update

set1.update(["w","e","o",9])
print(set1)

#length
print(len(set1))

#remove

set1.remove("v")
print(set1)

set1.discard("r")
print(set1)

set1.pop()
print(set1)

# set1.clear()
# del set1



#set operation

set2={1,4,3,6,7,8,2}
set3={1,4,6,7,8,9,6,4,3,2}

#union

set4=set2.union(set3)
print(set4)
#Or
set4=set3 |set2
#or
# set4=set3.update(set2)
# print(set4)


#diffrence

set5=set3-set2
print(set5)





lis=[1,3,5,6,9,8,4]
print(lis)
t=sorted(lis)
print(t[::-1])
