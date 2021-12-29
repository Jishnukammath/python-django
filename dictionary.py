dic={
    "apple":23,
    "banana":43,
    "orange":25
}
print(dic)

# dic.value,dic.keys
for i in dic.items():
    print(i)

del dic["apple"]
print(dic)

dic["graps"]=34
print(dic)

dic.pop()
print(dic)