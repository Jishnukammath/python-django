

# 1

l=[]
for i in range(10):
    l.append(i*i)
print(l)

li=[i*i for i in range(10)]
print(li)

#2

letters=[]
for i in "jishnukammath":
    letters.append(i)
print(letters)

lettrs=[i for i in "jishnu" ]
print(lettrs)

#3

evn=[]
odd=[]
for i in range(10):
    if i%2==0:
        evn.append(i)
    else:
        odd.append(i)

print(evn,odd)

even=[i for i in range(20) if i%2==0]
oddnum=[i for i in range(20) if i%2!=0]
print(even,oddnum)

#4

lists=[5,9,5,3,2,61,56,7,43,8]
even_square=[]
for i in lists:
    if (i*i)%2==0:
        even_square.append(i*i)
print(even_square)


lst=[i*i for i in lists if (i*i)%2==0]
print(lst)