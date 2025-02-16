# If Statement

is_hot = False
is_cold = False
if is_hot :
    print("Its a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("Its a cold day")
    print("Wear warm cloths")
else:
    print("Its a lovely day")

print("Enjoy your day")

# Exercise
price = 1000000
has_good_credit = False
if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print("Down Payment is :",down_payment)
