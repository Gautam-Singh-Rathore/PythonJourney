# Weight Converter

weight = input("Weight : ")
unit = input("(l)bs or (k)g:  ")

if unit=="L" or unit=='l':
    print(int(weight)*0.45)
elif unit=='K' or unit=='k':
    print(int(weight)/0.45)
else:
    print("Incorrect options selected : ")