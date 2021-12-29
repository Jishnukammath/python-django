dic1={
    1:"jishnu",
    2:"kammath",
    3:"jithin",
    4:"jishitha"
}
print(dic1)
print(dic1.get(2))
print(dic1.get(6,"item not get"))

for x in dic1:
    print(dic1[x])



if 2 in dic1:
    print("available")

print(len(dic1))

dic1.pop(2)
print(dic1)

dic1[5]="american apple"
print(dic1)

dic1.popitem()
print(dic1)


new_dic=dict(a="car",c="jeep")
print(new_dic)

dic2=dic1.copy()
print(dic2)
