t=(1,2,33,5,5,6,7,7,8,3,3,2,2,2)
print(t)
print(type(t))
print(len(t))


t1=("apple",22,55,"banana")
t3=t1+t
print(t3)
print(t3.count(2))
l=list(t)
l.append("fruit")
t=tuple(l)
print(t)