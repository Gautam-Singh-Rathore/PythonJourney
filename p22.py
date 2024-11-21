# Dictionaries

customer = {
    "name" : "Gautam Singh" ,
    "age" : 30 ,
    "is_verified": True
}

print(customer["name"])
customer["birthyear"]= "2023"
print(customer.get("birthyear" , "Jan 1 2024"))

# Exercise
words = ["zero" , "one","two" ,"three" ,"four" ,"five" ,"six" ,"seven" ,"eight" ,"nine"]
# We could have also used dictionary to store key value pairs
number = input("Phone : ")
ans = ""
for digit in number:
    index = int(digit)
    ans += words[index]+" "

print(ans)