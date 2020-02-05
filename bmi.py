# This program calculates somebody's Body Mass Index (BMI).
# The inputs are the person's height in centimetres and weight in kilograms.
# The output is their weight divided by their height in metres squared.


weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in centimetres: "))

hm2 = ((height / 100) **2)

BMI = weight / hm2
BMI2 = (round (BMI,2))

print("Your BMI is", BMI2)