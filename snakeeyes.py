import random

num1 = random.randint(1,6)
num2 = random.randint(1,6)

count=0

while(num1!=1 or num2!=1):
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    print("roll1 = "+str(num1) +" roll2 "+str(num2))
    count+=1
print(num1,num2)    
print("YA snake...")
print(count)
