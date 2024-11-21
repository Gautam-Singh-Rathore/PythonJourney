# List Methods
from os import remove

num =[1,9,3,8,5,6,4,7,7,2]
num.append(10)
num.insert(0,11)
num.remove(11)
#num.clear()
num.pop()
print(num.index(2))
print(15 in num)
print(num.count(7))
num.sort()
num.reverse()
num2 = num.copy()
print(num)

# Exercise
list = [2,2,4,6,3,4,6,1]
ans =[]
for item in list:
    if item not in ans:
        ans.append(item)

print(ans)

