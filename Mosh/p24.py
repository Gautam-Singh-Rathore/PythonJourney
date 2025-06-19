# Functions

def greet_user(first_name , last_name):
    print(f"hi {first_name} {last_name}")
    print("welcome abroad ")

print("Start")
greet_user("Gautam" , "Singh")
# Keyword Arguments
# Always use keyword arguments after positional arguments
greet_user(last_name="Singh" , first_name="John")
print("Finish")
