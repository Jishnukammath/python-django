
# division of two numbers

def div(number1,number2):
    try:
        result=number1//number2
        print(result)
    except:
        print("sorry..can't divided by zero")


number1=int(input("enter first number : "))
number2=int(input("enter second number : "))
div(number1,number2)
