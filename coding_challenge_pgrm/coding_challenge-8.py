
#List out  all the odd numbers from 1 to 100 using lists in Python,


odd_numbrs=[]

for i in range(100):
    if i%2!=0:
        odd_numbrs.append(i)

print(odd_numbrs)

#or

odd_num=[i for  i in range(100) if i%2!=0]
print(odd_num)
