

# BMI-calculator

def bmi_calc(w,h):
    b = w/(h**2)
    return b

weight = int(input("enter you weight in kg : "))
height = float(input("enter height in meter : "))

bmi = bmi_calc(weight,height)

print("BMI of the person is : ",bmi)