def multiply(*numbers):  # Tuple
    ans=1
    for num in numbers:
        ans *= num
    return ans

# print(multiply(2,3,4,5))

def save_user(**user):  # Dictionary
    print(user)
    print(user["id"])

save_user(id=1, standard=2 ,division=3)