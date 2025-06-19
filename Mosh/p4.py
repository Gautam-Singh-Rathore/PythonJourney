# Type Conversion

birth_year = input("Birth year :\n")
# Input function always returns a string
print(type(birth_year))
age = 2024 - int(birth_year)
print(age)

# Exercise
pound = input("Weight in pounds :\n")
kg = int(pound)*0.45
print("Your weight in kg is : " , kg)