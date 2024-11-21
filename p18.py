# Lists

names = ["Gautam" , "Devvrat" , "Gunjan" , "Ummed" , "Anil"]
print(names)
print(names[0]) # Don't modify the original list
print(names[-2])
print(names[2:4])

# Exercise
num = [2,3,4,5,6,7,8,9]
max = num[0]
for item in num:
    if item>max:
        max=item

print(max)