# Nested Loops

for x in range(4):
    for y in range(4):
        print(f"({x},{y})")

# Exercise ( F shape using nested loops )

for row in [5,2,5,2,2]:
    output = ''
    for column in range(row):
        output+='X'

    print(output)


