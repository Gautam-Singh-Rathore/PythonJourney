# Tuples are immutable
num = (1,2,3)
print(num)
print(num[0])

# Unpacking
coordinates = (1,2,3)
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]
print(x*y*z)

a,b,c = coordinates
print(a*b*c)
# This can be same done with lists
