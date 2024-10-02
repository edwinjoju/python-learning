weight = float(input("enter weight: "))
height = float(input("enter height: "))

bmi = (weight/((height/100)*2))
print(bmi)
if bmi < 16:
    print("severe underweight")
elif bmi > 16 and bmi < 18.4:
    print("underweight")
elif bmi > 18.5 and bmi < 24.9:
    print("normal")
elif bmi > 25 and bmi < 29.9:
    print("overweight")
elif bmi > 30 and bmi < 34.9:
    print("obese")
elif bmi > 35 and bmi < 39.9:
    print("severe obese")
else:
    print("dude ur fat as f***")