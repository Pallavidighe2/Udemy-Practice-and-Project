# def BMI (Weight,Height):
#     BMI=Weight/(Height)**2
#     return BMI
# BMI = BMI(49,158)
# print(BMI)

def BMI (Weight,Height):
    BMI=Weight/(Height**2)
    return BMI
Weight =float(input("Enter Weight in KG : "))
Height = float(input("Enter Height in Cm : "))

BMI=BMI(Weight,Height)
print(BMI)
