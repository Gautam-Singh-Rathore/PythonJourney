# Number Guessing game
secret_number = 9
count = 0
while count<3 :
    num = int(input("Guess : "))
    count+=1
    if num == secret_number:
        print("You won !!")
        break
else:
    print("Sorry you failed !!!")
