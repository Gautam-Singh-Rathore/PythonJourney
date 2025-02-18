msg="Hello"
def greet(name):
    global msg
    msg="Hii"

def send_email(name):
    msg="123@fake.com"

greet("Gautam")
print(msg) #-> Error because msg is a local variable