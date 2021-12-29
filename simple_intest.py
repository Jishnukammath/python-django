#calculate simple interest (p*n*r)/100

p=int(input("Enter principal amount : "))
n=int(input("Enter period of deposit in years : "))
r=int(input("Enter rate of interest : "))

interest=(p*n*r)/100

print("Simple Interest is :",interest)