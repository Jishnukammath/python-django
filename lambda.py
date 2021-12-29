

# x=lambda arg:expression

y=lambda a:a+3
print(y(6))

i=lambda a,b,c,d:a+3-b/c*d
print(i(6,4,2,2))


def mul(n,x):
    return lambda y:(y+x)*n
num=mul(10,8)
print(num(12))

num=mul(33,2)
print(num(22))
